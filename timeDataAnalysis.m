%% Analyize and compare Timeseries data

% Usages
% load tData.mat; 
% [ctData1 ctData2 ctData3] = timeDataAnalysis(tData1, tData2);

function [varargout] = timeDataAnalysis(varargin)

    [mm nn] = size(varargin);

    disp("N = "+nn);

    tData1 = varargin{1};
    tData2 = varargin{2};

    [tData3,tData4] = synchronize(tData2,tData1,'Uniform');

     figure(1);
     set(gcf,'color','w');
     grid on;
     tData2.plot;
     figure(2);
     set(gcf,'color','w');
     grid on;
     tData4.plot;


    hzdata = floor(tData1.Length / tData2.Length);

    varargout{1} = tData4;
    varargout{2} = tData3;
    varargout{3} = hzdata;

end