import cv2
import sys
import random
import math, time
sys.path.append("..")
import configparser
import numpy as np
import Mediapipe as mp
from pathlib import Path
from Mediapipe.fingerEnum import Finger, FingerCurled

def hex_to_rgb(value):
	"""
	Convert hex color codes into RGB format.

	Args:
		value: Hex color format.

	Returns:
		Output RGB format.
	"""
	value = value.lstrip('#')
	lv = len(value)
	return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


class HandModule(object) :
	# mediaPipe configuration hands object
	__mpHands = mp.solutions.hands
	# mediaPipe detector objet
	__mpHandDetector = None

	def __init__(self, max_num_object=2, model_path=None, detect_score = 0, track_score=0):
		self.class_names = ["five", "ya", "fist", "seven", "ok"]
		self.__mpHandDetector = self.__mpHands.Hands(
			max_num_hands= int(max_num_object),
			model_path= model_path,
			# Minimum confidence value ([0.0, 1.0]) from the landmark-tracking model for the hand landmarks to be considered tracked successfully (default= 0.5)
			min_detection_confidence= float(detect_score),
			# Minimum confidence value ([0.0, 1.0]) from the hand detection model for the detection to be considered successful. (default = 0.5)
			min_tracking_confidence= float(track_score)
		)
		self.finger_curled = [
			FingerCurled.NoCurl,
			FingerCurled.NoCurl,
			FingerCurled.NoCurl,
			FingerCurled.NoCurl,
			FingerCurled.NoCurl,
		]

	def __getEuclideanDistance(self, posA, posB):
		return math.hypot((posA.x - posB.x), (posA.y - posB.y))

	def __isThumbNearIndexFinger(self, thumbPos, indexPos):
		return self.__getEuclideanDistance(thumbPos, indexPos) < 0.1

	def __isFingerCurled(self, start_point, mid_point, end_point):
		start_mid_x_dist = start_point.x - mid_point.x
		start_end_x_dist = start_point.x - end_point.x
		mid_end_x_dist = mid_point.x - end_point.x

		start_mid_y_dist = start_point.y - mid_point.y
		start_end_y_dist = start_point.y - end_point.y
		mid_end_y_dist = mid_point.y - end_point.y

		start_mid_dist = math.sqrt(
			start_mid_x_dist ** 2 +
			start_mid_y_dist ** 2 )
		start_end_dist = math.sqrt(
			start_end_x_dist ** 2 +
			start_end_y_dist ** 2 )
		mid_end_dist = math.sqrt(
			mid_end_x_dist ** 2 +
			mid_end_y_dist ** 2 )

		cos_in = (mid_end_dist ** 2 + start_mid_dist ** 2 -
				  start_end_dist ** 2) / (2 * mid_end_dist * start_mid_dist+1e-10)
		if cos_in > 1.0:
			cos_in = 1.0
		elif cos_in < -1.0:
			cos_in = -1.0
		angle_of_curve = math.acos(cos_in)
		angle_of_curve = (57.2958 * angle_of_curve) % 180

		# print('Angle of curve = {}'.format(angle_of_curve))
		HALF_CURL_START_LIMIT = 60.0
		NO_CURL_START_LIMIT = 130.0

		finger_curled = None
		if angle_of_curve > NO_CURL_START_LIMIT:
			finger_curled = FingerCurled.NoCurl
		elif angle_of_curve > HALF_CURL_START_LIMIT:
			finger_curled = FingerCurled.HalfCurl
		else:
			finger_curled = FingerCurled.FullCurl

		return finger_curled
	
	def get_box(self, hand_landmarks, r=0.2):
		bbox = []
		for hand in hand_landmarks:
			bbox.append([hand.x, hand.y])
		bbox = np.array(bbox)
		centerX = (np.min(bbox[:,0]) + np.max(bbox[:,0])) / 2
		centerY = (np.min(bbox[:,1]) + np.max(bbox[:,1])) / 2
		width = (np.max(bbox[:,0]) - np.min(bbox[:,0]) )*(1+r)
		height = ( np.max(bbox[:,1]) - np.min(bbox[:,1]) )*(1+r)
		xmin = centerX - (width/2) 
		ymin = centerY - (height/2) 
		xmax =  centerX + (width/2) 
		ymax = centerY + (height/2) 
		detect_box = np.array([xmin, ymin, xmax, ymax])
		return detect_box

	def get_line(self, kpss):
		length = None
		thumb_finger_point, finger_middle_point, index_finger_point = None, None, None
		if kpss:
			# 获取大拇指指尖坐标
			thumb_finger_tip = kpss[4]
			thumb_finger_tip_x = math.ceil(thumb_finger_tip[0] )
			thumb_finger_tip_y = math.ceil(thumb_finger_tip[1] )
			# 获取食指指尖坐标
			index_finger_tip = kpss[8]
			index_finger_tip_x = math.ceil(index_finger_tip[0] )
			index_finger_tip_y = math.ceil(index_finger_tip[1] )
			# 中间点
			finger_middle_point = (thumb_finger_tip_x + index_finger_tip_x) // 2, (
					thumb_finger_tip_y + index_finger_tip_y) // 2
			# print(thumb_finger_tip_x)
			thumb_finger_point = (thumb_finger_tip_x, thumb_finger_tip_y)
			index_finger_point = (index_finger_tip_x, index_finger_tip_y)
	
			# 勾股定理计算长度
			length = int(math.hypot((index_finger_tip_x - thumb_finger_tip_x),
									(index_finger_tip_y - thumb_finger_tip_y)))
			
			# from numpy we find our length,by converting hand range in terms of volume range ie b/w -63.5 to 0
			# vol = np.interp(length,[20,150],[0, 100]) 

		return length, (thumb_finger_point, finger_middle_point, index_finger_point)

	def get_angle(self, kpss):
		bbox = []
		kpss_list = list(map(list, kpss))
		bbox = np.array(kpss_list)
		dx = bbox[9,0]-bbox[0,0]
		dy = bbox[9,1]-bbox[0,1]
		angle = np.arctan(dy/dx)
		angle = int(angle * 180 / math.pi)
		if (dx >=0) :
			angle += 90
		else :
			angle -= 90
		if (bbox[20, 0] >bbox[4, 0]) :
			angle += 5
		else :
			angle -= 10

		return angle

	def process(self, image):
		detectorResults = []
		if self.__mpHandDetector is None:
			return detectorResults

		detectorResults = self.__mpHandDetector.process(image)
		if detectorResults.multi_hand_landmarks:
			return detectorResults.multi_hand_landmarks
		else :
			return []

	def check_label(self, handLandmarks, print_finger_info=False):
		thumbIsOpen = False
		indexIsOpen = False
		middelIsOpen = False
		ringIsOpen = False
		pinkyIsOpen = False

		for finger in Finger:
			point_index_at = 0
			if finger == Finger.Thumb:
				point_index_at = 1
			finger_points_at = Finger.get_array_of_points(finger)
			start_point_at = handLandmarks[finger_points_at[point_index_at][0]]
			mid_point_at = handLandmarks[finger_points_at[point_index_at + 1][1]]
			end_point_at = handLandmarks[finger_points_at[3][1]]
			finger_curled = self.__isFingerCurled(start_point_at, mid_point_at, end_point_at)
			self.finger_curled[finger] = finger_curled

		for finger_index, curl in zip( Finger, self.finger_curled):
			if print_finger_info:
				print('Finger: {}, Curl: {}'.format(
						Finger.get_finger_name(finger_index), FingerCurled.get_finger_curled_name(curl)))
			
			if finger_index == Finger.Thumb and curl==FingerCurled.NoCurl :
				thumbIsOpen = True
			if curl in {FingerCurled.NoCurl, FingerCurled.HalfCurl}:
				if finger_index == Finger.Index :
					indexIsOpen = True
				elif finger_index == Finger.Middle :
					middelIsOpen = True
				elif finger_index == Finger.Ring :
					ringIsOpen = True
				elif finger_index == Finger.Pinky :
					pinkyIsOpen = True

		thumbindexlen = self.__getEuclideanDistance(handLandmarks[4], handLandmarks[5])
		indexpinkylen = self.__getEuclideanDistance(handLandmarks[5], handLandmarks[17])

		# print(thumbIsOpen, indexIsOpen, middelIsOpen, ringIsOpen, pinkyIsOpen)
		if thumbIsOpen and indexIsOpen and middelIsOpen and ringIsOpen and pinkyIsOpen:
			return self.class_names[0]

		# elif indexIsOpen and middelIsOpen and not thumbIsOpen and not ringIsOpen and not pinkyIsOpen :
		# 	return self.class_names[1]
	
		elif not indexIsOpen and not middelIsOpen and not ringIsOpen and not pinkyIsOpen and (not thumbIsOpen or thumbindexlen <= indexpinkylen ) :
			return self.class_names[2]

		elif thumbIsOpen and indexIsOpen and not middelIsOpen and not ringIsOpen and not pinkyIsOpen :
			return self.class_names[3]

		# elif not indexIsOpen and middelIsOpen and ringIsOpen and pinkyIsOpen and self.__isThumbNearIndexFinger(handLandmarks[4], handLandmarks[8]):
		# 	return self.class_names[4]

		return "unknown"


class FaceModule(object) :
	__mpFaces = mp.solutions.face_detection
	# mediaPipe detector objet
	__mpFaceDetector = None

	def __init__(self, model_path=None, detect_score=0.5):
		self.class_names = ["face"]
		self.__mpFaceDetector = self.__mpFaces.FaceDetection(
			model_path = model_path,
			# Minimum confidence value ([0.0, 1.0]) from the landmark-tracking model for the hand landmarks to be considered tracked successfully (default= 0.5)
			min_detection_confidence= float(detect_score),
		)
		
	def get_box(self, bbox):
		detect_box = []
		xmin, ymin = bbox.xmin, bbox.ymin
		xmax, ymax = bbox.xmin+bbox.width, bbox.ymin+bbox.height

		adjust = bbox.height/5
		ymin -= adjust
		detect_box = np.array([xmin, ymin, xmax, ymax])
		return detect_box

	def get_angle(self, kpss):
		kpss_list = list(map(list, kpss))
		bbox = np.array(kpss_list)
		dx = bbox[1,0]-bbox[0,0]
		dy = bbox[1,1]-bbox[0,1]
		angle = np.arctan(dy/dx)
		angle = int(angle * 180 / math.pi)
		if (dx >=0) :
			angle = angle
		else :
			angle = -angle
		return angle

	def process(self, image):
		detectorResults = []
		if self.__mpFaceDetector is None:
			return detectorResults

		detectorResults = self.__mpFaceDetector.process(image)
		if detectorResults.detections:
			return detectorResults.detections
		else :
			return []

	def check_label(self, handLandmarks):
		return self.class_names[0]


class MediapipeDetector(object):
	_defaults = {
		"binary_model_path": None,
		"detect_score" : None,
		"track_score" : None,
		"max_num_object" : None,
		"min_angle" : None,
		"max_angle" : None
	}

	@classmethod
	def set_defaults(cls, modelConfig) :
		if Path.is_file(Path(modelConfig)) :
			config = configparser.ConfigParser()
			config.read(modelConfig)
		else :
			print("Model .ini file not exist. Please check path.")
			time.sleep(2)
			sys.exit()
		defaults = {}
		for section in config.sections():
			for option in config.options(section):
				defaults[option] = config.get(section, option)
		cls._defaults = defaults

	def __init__(self, **kwargs):
		self.__dict__.update(self._defaults) # set up default values
		self.__dict__.update(kwargs) # and update with user overrides
		self.detector_type = None
		self.__setDefaultConfiguration()
		self.providers = 'CPUExecutionProvider'
		self.object_info = []
		
	def __setDefaultConfiguration(self):
		if ("hand_landmark" in self.binary_model_path) :
			self.Detector = HandModule(self.max_num_object, self.binary_model_path, self.detect_score, self.track_score)
			self.detector_type = "hand_landmark"
		elif ("face_detection" in self.binary_model_path) :
			self.Detector = FaceModule(self.binary_model_path, self.detect_score)
			self.detector_type = "face_detection"
		else :
			print("Detector type is not exist.")
			sys.exit()
		self.class_names = self.Detector.class_names
		self.class_names.append("unknown")
		get_colors = list(map(lambda i:"#" +"%06x" % random.randint(0, 0xFFFFFF),range(len(self.class_names)) ))
		self.colors_dict = dict(zip(list(self.class_names), get_colors))

	def draw_rotated_text(self, img, text, text_location, angle, color, *args, **kwargs):
		"""
		Draw Rotated Text on image.

		Args:
			img: Image.
			text: Text string to be drawn.
			text_location: Bottom-left corner of the text string in the image.
			angle: minus angle is Quadrant II/III  | plus angle is Quadrant I/IV 
			color: Text color.

		Returns:
			Output frame results
		"""
		mask_text = np.zeros(img.shape, dtype=np.uint8)

		cv2.putText(mask_text, text, text_location, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

		# Rotate the image using cv2.warpAffine()
		M = cv2.getRotationMatrix2D( (int(text_location[0]), int(text_location[1])), -angle, 1)
		mask = cv2.warpAffine(mask_text, M, (img.shape[1], img.shape[0]))
		ret, mask_boolean = cv2.threshold(mask , 127, 254, cv2.THRESH_BINARY)
		out = np.array(img).astype(int) * np.array(mask_boolean+1).astype(int)
		out[out>=255]=255
		return out.astype(np.uint8)

	def draw_rotated_rect(self, img, pt1_point, pt3_point, angle, label, color=(255, 255, 255), thickness=2):
		"""
		Draw Rotated Rect on image.

		Args:
			img: Image.
			pt1_point: Vertex of the rectangle.
			pt3_point: Vertex of the rectangle opposite to pt1 .
			angle: minus angle is Quadrant II/III  | plus angle is Quadrant I/IV 
			label: Calc text length to fill label background color.
			color: Rectangle color or brightness (grayscale image).
			thickness: Thickness of lines that make up the rectangle. Negative values, like #FILLED, mean that the function has to draw a filled rectangle.

		Returns:
			pt1: Get left-top (x, y) values.
			pt2: Get right-top (x, y) values.
		"""
		(xmin, ymin) = pt1_point
		(xmax, ymax) = pt3_point

		center_x = (xmax+xmin)/2
		center_y = (ymax+ymin)/2
		height = ymax - ymin
		width = xmax - xmin

		_angle = angle * math.pi / 180.0
		b = math.cos(_angle) * 0.5
		a = math.sin(_angle) * 0.5
		pt0 = (int(center_x - a * height - b * width),
			int(center_y + b * height - a * width))
		pt1 = (int(center_x + a * height - b * width),
			int(center_y - b * height - a * width))
		pt2 = (int(2 * center_x - pt0[0]), int(2 * center_y - pt0[1]))
		pt3 = (int(2 * center_x - pt1[0]), int(2 * center_y - pt1[1]))

		cv2.line(img, pt0, pt1, color, thickness)
		cv2.line(img, pt1, pt2, color, thickness)
		cv2.line(img, pt2, pt3, color, thickness)
		cv2.line(img, pt3, pt0, color, thickness)

		# calc_label_rect
		if (label) :
			tl = 3 or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line thickness
			tf = max(tl - 1, 1)  # font thickness
			t_size = cv2.getTextSize(label, 0, fontScale=tl / 2, thickness=tf)[0]
			for offset in range(0, 30, 2):
				pt_offset = (int(center_x - a * (height+2*offset )  - b * t_size[0] ),
							int((center_y-(offset /2))  + b * (height+offset )  - a * t_size[0] ))
				label_start = (int(center_x  + a * (height+2*offset) - b * width ),
						int(center_y-(offset /2) - b * (height+offset ) - a * width))
				label_end = (int(2 * center_x- pt_offset[0]  ), int(2 * (center_y-(offset /2)) - pt_offset[1]) )
				cv2.line(img, label_start, label_end, color, thickness)

		return pt1, pt2
	
	def get_boxes_coordinate(self, bounding_boxes, ratiow, ratioh):
		"""
		Parse the original size box.

		Args:
			bounding_boxes: [xmin, ymin, xmax, ymax].
			ratiow: Original img width.
			ratioh: Original img height.

		Returns:
			return box [xmin, ymin, xmax, ymax]
		"""
		bounding_boxes[0] = int(bounding_boxes[0] * ratiow )
		bounding_boxes[1] = int(bounding_boxes[1] * ratioh )
		bounding_boxes[2] = int(bounding_boxes[2] * ratiow )
		bounding_boxes[3] = int(bounding_boxes[3] * ratioh )
		return bounding_boxes.astype(int)

	def get_kpss_coordinate(self, handLandmarks, ratiow, ratioh):
		"""
		Parse the original size key-points.

		Args:
			bounding_boxes: Mediapipe output landmarks.
			ratiow: Original img width.
			ratioh: Original img height.

		Returns:
			return box [(x1, y1), (x2, y2) ... (xn, yn)]
		"""
		kpss = []
		for handLandmark in handLandmarks :
			kpss.append( (int(handLandmark.x*ratiow), int(handLandmark.y*ratioh)) )
		return kpss

	def DetectFrame(self, image):
		"""
		Calculate detection results.

		Args:
			image: Image.

		Returns:
			None
		"""
		self.object_info = []
		min_angle = int(self.min_angle)
		max_angle = int(self.max_angle)

		# Input image must contain three channel rgb data.
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		ratioh, ratiow = image.shape[0], image.shape[1]
		# lock image for hand detection
		image.flags.writeable = False
		# start handDetector on current image
		nms_results = self.Detector.process(image)
		# unlock image
		image.flags.writeable = True

		if len(nms_results) > 0:
			for Landmarks in nms_results:
				landmark = []
				if (self.detector_type == "hand_landmark") :
					landmark = Landmarks.landmark
					# classification.classification[0].label
					detect_box = self.Detector.get_box(landmark)
				elif (self.detector_type == "face_detection" ) :
					landmark = Landmarks.location_data.relative_keypoints
					detect_box = self.Detector.get_box(Landmarks.location_data.relative_bounding_box)

				label = self.Detector.check_label(landmark)
				bounding_boxes = self.get_boxes_coordinate( detect_box, ratiow, ratioh)
				kpss = self.get_kpss_coordinate(landmark, ratiow, ratioh)
				angle = self.Detector.get_angle(kpss)
				if (angle >= min_angle and angle <= max_angle) or (angle <= -min_angle and angle >= -max_angle):
					if ( bounding_boxes[0] >=0 and bounding_boxes[1] >= 0 and bounding_boxes[3] <= image.shape[0] and bounding_boxes[2] <= image.shape[1]):
						self.object_info.append(([bounding_boxes[1], bounding_boxes[0], bounding_boxes[3], bounding_boxes[2], label], kpss, angle))

	def GetSliderFromLandmark(self, frame_show) :
		"""
		Get Length Between Thumb and Index Finger.

		Args:
			frame_show: img.

		Returns:
			return two points length 
		"""
		slider_len = None
		if (self.detector_type == "hand_landmark") :
			if ( len(self.object_info) != 0 )  :
				for _, kpss, angle in self.object_info:
					if (len(kpss) != 0) :
						slider_len, (thumb_finger_point, finger_middle_point, index_finger_point) = self.Detector.get_line(kpss)
						# 画2点连线
						cv2.line(frame_show, thumb_finger_point, index_finger_point, (255, 0, 255), 3)
						# 画指尖2点
						cv2.circle(frame_show, thumb_finger_point, 6, (255, 0, 255), -1)
						cv2.circle(frame_show, index_finger_point, 6, (255, 0, 255), -1)
						cv2.circle(frame_show, finger_middle_point, 4, (255, 0, 0), -1)
		return slider_len

	def DrawDetectedOnFrame(self, frame_show, thickness=2) :
		"""
		Draw results on image.

		Args:
			frame_show: Image.
			thickness: Thickness of lines that make up the rectangle.

		Returns:
			Output frame results
		"""
		if ( len(self.object_info) != 0 )  :
			for box, kpss, angle in self.object_info:
				ymin, xmin, ymax, xmax, label = box
				if (len(kpss) != 0) :
					for kp in kpss :
						cv2.circle(frame_show,  kp, 1, (255, 255, 255), thickness=-1)

				(xmin, ymin), _ = self.draw_rotated_rect(frame_show, (xmin, ymin), (xmax, ymax), angle, label, hex_to_rgb(self.colors_dict[label]), thickness)
				frame_show = self.draw_rotated_text(frame_show, label, (xmin, ymin - 5), angle, (255, 255, 255))
				
		return frame_show


if __name__ == "__main__":
	# cap = cv2.VideoCapture(r"D:\Jimmy\SmartVideoPlayer\stm32拍摄建模视频.mp4")
	cap = cv2.VideoCapture(0)
	modelConfig = './face_inference.ini'
	MediapipeDetector.set_defaults(modelConfig)
	faceDetector =  MediapipeDetector()

	modelConfig = './hand_inference.ini'
	MediapipeDetector.set_defaults(modelConfig)
	handDetector =  MediapipeDetector()

	while cap.isOpened():
		success, image = cap.read()
		if not success:
			print("Ignoring empty camera frame.")
			# If loading a video, use 'break' instead of 'continue'.
			break
		faceDetector.DetectFrame(image)
		image = faceDetector.DrawDetectedOnFrame(image)

		handDetector.DetectFrame(image)
		image = handDetector.DrawDetectedOnFrame(image)
		handDetector.GetSliderFromLandmark(image)

		cv2.imshow('MediaPipe Hands', image)
		if cv2.waitKey(5) & 0xFF == 27:
			break