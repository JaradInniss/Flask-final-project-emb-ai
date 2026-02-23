from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        # Test for Joy
        statement = "I am glad this happened"
        dominant_emotion = emotion_detector(statement)
        self.assertEqual(dominant_emotion['dominant_emotion'], 'joy')

    def test_anger(self):
        # Test for Anger
        statement = "I am really mad about this"
        dominant_emotion = emotion_detector(statement)
        self.assertEqual(dominant_emotion['dominant_emotion'], 'anger')

    def test_disgust(self):
        # Test for Disgust
        statement = "I feel disgusted just hearing about this"
        dominant_emotion = emotion_detector(statement)
        self.assertEqual(dominant_emotion['dominant_emotion'], 'disgust')

    def test_sadness(self):
        # Test for Sadness
        statement = "I am so sad about this"
        dominant_emotion = emotion_detector(statement)
        self.assertEqual(dominant_emotion['dominant_emotion'], 'sadness')

    def test_fear(self):
        # Test for Fear
        statement = "I am really afraid that this will happen"
        dominant_emotion = emotion_detector(statement)
        self.assertEqual(dominant_emotion['dominant_emotion'], 'fear')

unittest.main()

