import cv2
import sys
import random
import math, time
from pathlib import Path
sys.path.append("..")
import configparser
import numpy as np
import Mediapipe as mp

def hex_to_rgb(value):
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
		
	def __getEuclideanDistance(self, posA, posB):
		return math.sqrt((posA.x - posB.x)**2 + (posA.y - posB.y)**2)

	def __isThumbNearIndexFinger(self, thumbPos, indexPos):
		return self.__getEuclideanDistance(thumbPos, indexPos) < 0.1

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

	def get_line(self, hand_landmarks):
		line_len = None
		thumb_finger_point, finger_middle_point, index_finger_point = None, None, None
		if hand_landmarks:
			# 获取大拇指指尖坐标
			thumb_finger_tip = hand_landmarks[4]
			thumb_finger_tip_x = math.ceil(thumb_finger_tip[0] )
			thumb_finger_tip_y = math.ceil(thumb_finger_tip[1] )
			# 获取食指指尖坐标
			index_finger_tip = hand_landmarks[8]
			index_finger_tip_x = math.ceil(index_finger_tip[0] )
			index_finger_tip_y = math.ceil(index_finger_tip[1] )
			# 中间点
			finger_middle_point = (thumb_finger_tip_x + index_finger_tip_x) // 2, (
					thumb_finger_tip_y + index_finger_tip_y) // 2
			# print(thumb_finger_tip_x)
			thumb_finger_point = (thumb_finger_tip_x, thumb_finger_tip_y)
			index_finger_point = (index_finger_tip_x, index_finger_tip_y)

			# 勾股定理计算长度
			line_len = int(math.hypot((index_finger_tip_x - thumb_finger_tip_x),
									(index_finger_tip_y - thumb_finger_tip_y)))

		return line_len, (thumb_finger_point, finger_middle_point, index_finger_point)

	def get_angle(self, kpss):
		bbox = []
		kpss_list = list(map(list, kpss))
		bbox = np.array(kpss_list)
		dx = bbox[12,0]-bbox[0,0]
		dy = bbox[12,1]-bbox[0,1]
		angle = np.arctan(dy/dx)
		angle = int(angle * 180 / math.pi)
		if (dx >=0) :
			angle += 90
		else :
			angle -= 90
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

	def check_label(self, handLandmarks):

		thumbIsOpen = False
		indexIsOpen = False
		middelIsOpen = False
		ringIsOpen = False
		pinkyIsOpen = False

		if (handLandmarks[0].x < handLandmarks[1].x) :
			right = True
			left = False
		else :
			right = False
			left = True

		# pinky
		pseudoFixKeyPoint = handLandmarks[18].y
		if ( handLandmarks[19].y < handLandmarks[0].y) :
			if handLandmarks[19].y <= pseudoFixKeyPoint and handLandmarks[20].y <= pseudoFixKeyPoint:
				pinkyIsOpen = True
		else :
			pseudoFixKeyPoint = handLandmarks[18].x
			if handLandmarks[19].x < pseudoFixKeyPoint and handLandmarks[20].x < pseudoFixKeyPoint and right :
				pinkyIsOpen = True
			elif handLandmarks[19].x > pseudoFixKeyPoint and handLandmarks[20].x > pseudoFixKeyPoint and left :
				pinkyIsOpen = True

		# ring
		pseudoFixKeyPoint = handLandmarks[14].y
		if handLandmarks[15].y < pseudoFixKeyPoint and handLandmarks[16].y < pseudoFixKeyPoint:
			ringIsOpen = True

		# middel
		pseudoFixKeyPoint = handLandmarks[10].y
		if handLandmarks[11].y < pseudoFixKeyPoint and handLandmarks[12].y < pseudoFixKeyPoint:
			middelIsOpen = True

		# index
		pseudoFixKeyPoint = handLandmarks[6].y
		if handLandmarks[7].y < pseudoFixKeyPoint and handLandmarks[8].y < pseudoFixKeyPoint:
			indexIsOpen = True

		# thumb
		pseudoFixKeyPoint = handLandmarks[2].x
		if handLandmarks[3].x < pseudoFixKeyPoint and handLandmarks[4].x < pseudoFixKeyPoint : 
			if (left) :
				thumbIsOpen = True
			if (right and handLandmarks[4].y < handLandmarks[5].y and indexIsOpen  ) :
				thumbIsOpen = True
		elif handLandmarks[3].x > pseudoFixKeyPoint and handLandmarks[4].x > pseudoFixKeyPoint :
			if (left and handLandmarks[4].y < handLandmarks[5].y and indexIsOpen  ) :
				thumbIsOpen = True
			if (right) :
				thumbIsOpen = True

		# print(thumbIsOpen, indexIsOpen, middelIsOpen, ringIsOpen, pinkyIsOpen)
		thumbindexlen = abs(handLandmarks[4].x - handLandmarks[5].x)
		indexpinkylen = abs(handLandmarks[5].x - handLandmarks[17].x) 

		if thumbIsOpen and indexIsOpen and middelIsOpen and ringIsOpen and pinkyIsOpen:
			return self.class_names[0]

		# elif indexIsOpen and middelIsOpen and not thumbIsOpen and not ringIsOpen and not pinkyIsOpen :
		# 	return self.class_names[1]

		elif not indexIsOpen and not middelIsOpen and not ringIsOpen and not pinkyIsOpen and ( not thumbIsOpen and thumbindexlen <= indexpinkylen ) :
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

	def get_boxes_coordinate(self, bounding_boxes, ratiow, ratioh):
		bounding_boxes[0] = int(bounding_boxes[0] * ratiow )
		bounding_boxes[1] = int(bounding_boxes[1] * ratioh )
		bounding_boxes[2] = int(bounding_boxes[2] * ratiow )
		bounding_boxes[3] = int(bounding_boxes[3] * ratioh )
		return bounding_boxes.astype(int)

	def get_kpss_coordinate(self, handLandmarks, ratiow, ratioh):
		kpss = []
		for handLandmark in handLandmarks :
			kpss.append( (int(handLandmark.x*ratiow), int(handLandmark.y*ratioh)) )
		return kpss

	def DetectFrame(self, image):
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
					detect_box = self.Detector.get_box(landmark)
				elif (self.detector_type == "face_detection" ) :
					landmark = Landmarks.location_data.relative_keypoints
					detect_box = self.Detector.get_box(Landmarks.location_data.relative_bounding_box)

				label = self.Detector.check_label(landmark)
				bounding_boxes = self.get_boxes_coordinate( detect_box, ratiow, ratioh)
				kpss = self.get_kpss_coordinate(landmark, ratiow, ratioh)
				angle = self.Detector.get_angle(kpss)
				if (angle >= min_angle and angle <= max_angle) or (angle <= -min_angle and angle >= -max_angle):
					self.object_info.append(([bounding_boxes[1], bounding_boxes[0], bounding_boxes[3], bounding_boxes[2], label], kpss, angle))

	def GetSliderFromLandmark(self, frame_show) :
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
		tl = 3 or round(0.002 * (frame_show.shape[0] + frame_show.shape[1]) / 2) + 1  # line/font thickness
		if ( len(self.object_info) != 0 )  :
			for box, kpss, angle in self.object_info:
				ymin, xmin, ymax, xmax, label = box
				if (len(kpss) != 0) :
					for kp in kpss :
						cv2.circle(frame_show,  kp, 1, (255, 255, 255), thickness=-1)
				c1, c2 = (xmin, ymin), (xmax, ymax)        
				tf = max(tl - 1, 1)  # font thickness
				t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
				c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3

				if (label != 'unknown') :
					cv2.rectangle(frame_show, c1, c2, hex_to_rgb(self.colors_dict[label]), -1, cv2.LINE_AA)
					cv2.rectangle(frame_show, (xmin, ymin), (xmax, ymax), hex_to_rgb(self.colors_dict[label]), thickness)
				else :
					cv2.rectangle(frame_show, c1, c2, (0, 0, 0), -1, cv2.LINE_AA)
					cv2.rectangle(frame_show, (xmin, ymin), (xmax, ymax), (0, 0, 0), thickness)
				cv2.putText(frame_show, label, (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


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
		faceDetector.DrawDetectedOnFrame(image)

		handDetector.DetectFrame(image)
		handDetector.DrawDetectedOnFrame(image)
		handDetector.GetSliderFromLandmark(image)

		cv2.imshow('MediaPipe Hands', image)
		if cv2.waitKey(5) & 0xFF == 27:
			break