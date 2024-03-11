%% Single-Input Multi-output custom deep learning

clc; clear all; close all;


%% Data loading
load multiData.mat; 

%% Data segmentation
[m n]= size(xRand);

seqIndex = randperm(m)';

xData = [];
yData = [];

for i=1:m
    xData = [xData; xRand(seqIndex(i),:)];
    yData = [yData; yRand(seqIndex(i),:)];
end

m1 = floor(m*0.8);

maxX = max(max(xData));
maxY = max((max(abs(yData))));

xData = xData./maxX;
yData = yData./maxY;

xTraining = xData(1:m1,:);
yTraining = yData(1:m1,:);

xTest = xData(m1+1:end,:);
yTest = yData(m1+1:end,:);

%% Multi deep learning architecture

layers1 = [
    featureInputLayer(15,"Name","featureinput")
    fullyConnectedLayer(20,"Name","fc")
    tanhLayer("Name","tanh")
    fullyConnectedLayer(16,"Name","fc_1")
    tanhLayer("Name","tanh_1")
    fullyConnectedLayer(12,"Name","fc_2")
    tanhLayer("Name","tanh_2")
    fullyConnectedLayer(9,"Name","fc_3")
    tanhLayer("Name","tanh_3")
    fullyConnectedLayer(6,"Name","fc_4")
    tanhLayer("Name","tanh_4")
    fullyConnectedLayer(3,"Name","fc_5")
    tanhLayer("Name","tanh_5")
    fullyConnectedLayer(1,"Name","fc_6")
    ];

lgraph = layerGraph(layers1);


layers2 = [ fullyConnectedLayer(6,"Name","fc_7")
    tanhLayer("Name","tanh_7")
    fullyConnectedLayer(3,"Name","fc_8")
    tanhLayer("Name","tanh_8")
    fullyConnectedLayer(1,"Name","fc_9")
    ];

lgraph = addLayers(lgraph,layers2);


lgraph = connectLayers(lgraph,"tanh_3","fc_7");





figure(1);
set(gcf,'color',[1 1 1]);
plot(lgraph);

%% Deep learning network

net = dlnetwork(lgraph);

%%

xxx = dlarray(double(xTraining),'BC');
yy1 = dlarray(double(yTraining(:,1)),'BC');
yy2 = dlarray(double(yTraining(:,2)),'BC');



%% Deep learnign options

numEpochs = 100;

monitor = trainingProgressMonitor(Metrics="Loss", Info="Epoch", XLabel="Iteration");


epoch = 0;
iteration = 1;
numIterations = 100;

averageGrad = [];
averageSqGrad = [];

lossAll = [];

for i=1:(numEpochs-1)

    [loss, gradients,state] = dlfeval(@modelLoss,net,xxx,yy1,yy2);
    net.State = state;

    lossAll = [lossAll; loss];

    [net,averageGrad,averageSqGrad] = adamupdate(net,gradients,averageGrad,averageSqGrad,iteration);

    iteration = iteration +1;

          recordMetrics(monitor,iteration,Loss=loss);
        updateInfo(monitor,Epoch=epoch + " of " + numEpochs);
        monitor.Progress = 100 * iteration/numIterations;
        epoch = epoch+1;
end




%%

function [loss, gradients, state] = modelLoss(net,X,target1, target2)

    [y1, y2, state] = forward(net,X, outputs = ["fc_6" "fc_9"] );

    lossLabel1 = mse(y1, target1);
    lossLabel2 = mse(y2, target2);

    loss = 0.6*lossLabel1 + 0.4*lossLabel2;
    gradients = dlgradient(loss,net.Learnables);


end

