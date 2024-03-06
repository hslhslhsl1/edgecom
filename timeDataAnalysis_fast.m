%% Analyize and compare Timeseries data for fast processing

% Usages
% load tData.mat; 
% [ctData1 ctData2 ctData3] = timeDataAnalysis(tData1, tData2);

function [varargout] = timeDataAnalysis_fast(varargin)

    [mm nn] = size(varargin);

    disp("N = "+nn);

    tData1 = varargin{1};
    tData2 = varargin{2};

    [tData3,tData4] = synchronize(tData2,tData1,'Uniform');


    hzdata = floor(tData1.Length / tData2.Length);

    varargout{1} = tData4;
    varargout{2} = tData3;
    varargout{3} = hzdata;

end