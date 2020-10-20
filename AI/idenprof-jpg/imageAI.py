# pip3 install tensorflow==1.13.1
# pip3 install opencv-python
# pip3 install keras==2.2.4
# pip3 install numpy==1.16.1
# pip3 install imageai --upgrade

from imageai.Prediction.Custom import ModelTraining
import os

# print(os.getcwd()+"\Desktop\AI\idenprof-jpg\idenprof\test")
# for subdir in sorted(os.listdir("idenprof")):
#     print(subdir)

#TRAINING OUR AI ##NOT RUNNING IT SINCE IT TAKES 2 HOURS TO TRAIN
#model_trainer = ModelTraining()
#model_trainer.setModelTypeAsResNet()
#model_trainer.setDataDirectory(os.getcwd()+"\Desktop\AI\idenprof-jpg\idenprof\test")
#model_trainer.trainModel(num_objects=10, num_experiments=200, enhance_data=True, batch_size=32, show_network_summary=True)











from imageai.Prediction.Custom import CustomImagePrediction
import os

execution_path = os.getcwd()

#CREATE OUR AI OBJECT
prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.getcwd()+"\Desktop\AI\idenprof-jpg\idenprof_061-0.7933.h5")
prediction.setJsonPath(os.getcwd()+ "\Desktop\AI\idenprof-jpg\idenprof_model_class.json")
prediction.loadModel(num_objects=10)

#INTERACT WITH OUR AI
# print(os.getcwd()+"\Desktop\IT\image\idenprof" + "\\test\chef\chef-1.jpg")
predictions, probabilities = prediction.predictImage(os.getcwd()+"\Desktop\AI\idenprof-jpg\idenprof\\test\chef\chef-5.jpg", result_count=3)
for eachPrediction, eachProbability in zip(predictions, probabilities): #DISPLAY TOP 3 PREDICTIONS 
    print(eachPrediction , " : " , eachProbability)

