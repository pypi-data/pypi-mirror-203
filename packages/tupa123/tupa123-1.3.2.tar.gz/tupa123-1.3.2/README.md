Fully connected four-layer neural network <br>
Solves a huge number of cases, classification and regression <br>
The following sequence explains how to use with the help of two example files. <br>
The first file contains the learning process, where the neural network finds its weights <br>
The second file demonstrates the network's ability to make predictions on new, unseen data that is not part of the training set <br>
<br>
<br>
#Manual = https://www.mediafire.com/file/xygt3o9zf7iw3id/Manual_Tupa123.pdf <br>
<br>
#Excel example data = https://www.mediafire.com/file/o2nzsmnvweh8w1a/ALETAS.xlsx<br>
#Excel example (old version) = https://www.mediafire.com/file/0xmx5quakd21txu/ALETAS.xls <br>
<br>
<br>
#<b>-----Files without comments:--------------------------------------- </b><br>
<br>
#-----FILE TO MACHINE LEARNING <br>
<br>
import tupa123 as tu <br>
<br>
X = tu.ExcelMatrix('ALETAS.xlsx', 'Plan1', Lineini=2, Columini=1, columnquantity=5, linesquantity=300) <br>
y = tu.ExcelMatrix('ALETAS.xlsx', 'Plan1', Lineini=2, Columini=6, columnquantity=2, linesquantity=300) <br>
<br>
model = tu.nnet4(norma=5, coef=0, nn1c=5, nn2c=7, nn3c=5, nn4c=2, rate=0.01, epochs=1000, fa2c=5, fa3c=5, fa4c=0) <br>
model.Fit_ADAM(X, y) <br>
model.Plotconv() <br>
<br>
input('end') <br>
<br>
#-----FILE TO APPLICATION OF MACHINE LEARNING <br>
<br>
import tupa123 as tu <br>
<br>
model = tu.nnet4(norma=5, coef=0, normout=1, nn1c=5, nn2c=7, nn3c=5, nn4c=2, fa2c=5, fa3c=5, fa4c=0) <br>
X_new = tu.ExcelMatrix('ALETAS.xlsx', 'Plan1', Lineini=2, Columini=1, columnquantity=5, linesquantity=1000) <br>
y_resposta = tu.ExcelMatrix('ALETAS.xlsx', 'Plan1', Lineini=2, Columini=6, columnquantity=2, linesquantity=1000) <br>
y_pred = model.Predict(X_new) <br>
<br>
tu.Statistics(y_pred, y_resposta) <br>
tu.PlotCorrelation(y_pred, y_resposta) <br>
tu.PlotComparative(y_pred, y_resposta) <br>
input('end') <br>
<br>
#<b>------Commented file:------------------------------------------</b> <br>
<br>
#-----MACHINE LEARNING <br>
<br>
<b>import tupa123 as tu</b> <br>
#import the library <br>
<br>
<b>X = tu.ExcelMatrix('ALETAS.xlsx', 'Plan1', Lineini=2, Columini=1, columnquantity=5, linesquantity=300)</b> <br>
<b>y = tu.ExcelMatrix('ALETAS.xlsx', 'Plan1', Lineini=2, Columini=6, columnquantity=2, linesquantity=300)</b> <br>
#learning data <br>
#The data can come from any source, but the ExcelMatrix function allows a practical interaction with Excel <br>
#ExcelMatrix = collect data from excel, the spreadsheet needs to be in the same folder as the python file <br>
#'ALETAS.xlsm' = example name of the excel file / 'Sheet1' = example name of the tab where the data are <br>
#Lineini=2, Columini=1 = example initial row and column of data <br>
#linesquantity = number of lines of learning data <br>
#X = regression input data / y = data to be predicted <br>
<br>
<b>model = tu.nnet4(norma=5, coef=0, normout=1, nn1c=5, nn2c=7, nn3c=5, nn4c=2, rate=0.01, epochs=1000, fa2c=5, fa3c=5, fa4c=0, cost=0, regu=0, namenet='')</b> <br>
#creates the Neural Network model <br>
<br>
#norma = type of data normalization: (default=2)<br>
#=-1, standardization <br>
#=0, do anything <br>
#=1, between 0 and 1 <br>
#=2, between -1 and 1 <br>
#=3, log(x+coef) <br>
#=4, log(x+coef)  between 0 and 1 <br>
#=5, log(x+coef)  between -1 and 1 <br>
#=6, log(x+coef)  and standardization <br>
#coef = used to avoid zero in log normalizations, example 0.0012345 (default=0)<br>
#normout = if 1 normalizes the output (default=1), 0 dont <br>
<br>
#nn1c=5, nn2c=7, nn3c=5, nn4c=2 = number of neurons from the first to the fourth layer (default=1,5,5,1) <br>
#rate = learning rate (default=0.01) <br>
#epochs = number of epochs (default=1000)<br>
#fa2c=5, fa3c=5, fa4c=0 = second to fourth layer activation functions (default=5,5,0) <br>
#for regression the fourth layer is recommended as linear = 0 <br>
#cost=0, cost function, (default=0). 0 = MSE, mean squared error for regression and classification / 1 = BCE, binary cross entropy for classification <br>
#regu= regularization, (default=0). Usual value for regression = 0.01 <br>
#namenet= name of the folder where the weights are saved, default is the same directory as the .py file, necessary when working with more than one neural network <br>
<br>
#Activation functions: <br>
#=0 linear <br> 
#=1 Sigmoide <br>
#=2 softpluss <br>
#=3 gaussinana <br>
#=4 ReLU <br>
#=5 tanh <br>
#=6 LReLU <br>
#=7 arctan <br>
#=8 exp <br>
#=9 seno <br>
#=10 swish <br>
#=11 selu <br>
#=12 logsigmoide <br>
#=13 X**2 <br>
#=14 X**3 <br>
#=15 Symmetric Rectified Linear <br>
<br>
<b>model.Fit_ADAM(X, y) </b><br>
#machine learning <br>
#model.Fit_ADAM(X, y) = single batch interpolation of all learning data, with ADAM accelerator <br>
#model.Fit_STOC(X, y) = case-by-case interpolation, stochastic gradient descent <br>
#model.Fit_STOC_ADAM(X, y) = case-by-case interpolation, stochastic with ADAM <br>
<br>
<b>model.Plotconv()</b> <br>
#Plot the convergence process <br>
<br>
input('End') <br>
<br>
#-----APPLICATION OF MACHINE LEARNING <br>
<br>
<b>import tupa123 as tu</b> <br>
<br>
<b>model = tu.nnet4(norma=5, coef=0, nn1c=5, nn2c=7, nn3c=5, nn4c=2, fa2c=5, fa3c=5, fa4c=0) </b><br>
#application file must be in the same folder as the learning file <br>
#where some .txt files were generated with the neural network settings <br>
#neural network must have the same configuration that was used in the learning phase <br>
<br>
<b>X_new = tu.ExcelMatrix('ALETAS.xlsx', 'Plan1', Lineini=2, Columini=1, columnquantity=5, linesquantity=1000)</b> <br>
#variables to be predicted <br>
<br>
<b>y_resposta = tu.ExcelMatrix('ALETAS.xlsx', 'Plan1', Lineini=2, Columini=6, columnquantity=2, linesquantity=1000) </b><br>
#right answer to compare, to evaluate neural network performance <br>
<br>
<b>y_pred = model.Predict(X_new) </b><br>
#prediction, neural network result <br>
<br>
<b>tu.Statistics(y_pred, y_resposta) </b><br>
#Statistical evaluation of the results <br>
#It does some basic statistics: mean difference, standard deviation and correlation coefficient between predicted and target variable <br>
<br>
<b>tu.PlotCorrelation(y_pred, y_resposta) </b><br>
#Calculated and target correlation plot <br>
<br>
<b>tu.PlotCorrelation2(y_pred, y_resposta) </b><br>
#Calculated and target correlation plot with standard deviation lines<br>
<br>
<b>tu.PlotComparative(y_pred, y_resposta) </b><br>
#Calculated and target comparative plot <br>
<br>
<b>tu.PlotComparative2(y_pred, y_resposta, window_size=1000) </b><br>
#Error plot with movel average<br>
<br>
<b>tu.PlotComparative3(y_pred, y_resposta) </b><br>
#Calculated and target comparative plot with standard deviation areas <br>
<br>
<b>tu.PlotComparative4(y_pred, y_resposta) </b><br>
#Plot 2 sigma tandard deviation areas with target <br>
<br>
<b>tu.PlotDispe(y_pred, y_resposta) </b><br>
#Error dispersion <br>
<br>
<b>tu.PlotDispe2(y_pred, y_resposta) </b><br>
#Error dispersion with error proportion<br>
<br>
<b>tu.PlotHisto(y_pred, y_resposta) </b><br>
#Percentage error histogram <br>
<br>
input('end') <br>