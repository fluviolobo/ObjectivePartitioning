% =========================================================================
%
% roiratios.m
%
% Region of Iterest (ROI) Ratios
%
% The function computes the ratio between desired/listed means of physical
% parameters, at specific simulation states. The output table contains the
% simulation state (1st column) and the result of the ratio (2nd column).
%
% Fluvio Lobo Fenoglietto
%
% =========================================================================

function [ratios] = roiratios(ele,states,physics,numerator,denominator)
    % Length of input arrays
    Nstates = length(states); % Double Array
    Nfiles = length(physics); % Cell Array
    Npartitions = length(numerator); % Cell Array   
    ratios = zeros(Nstates,2);    
    for h = 1:Nstates % Loop around Simulation States     
        state_label = strcat('state',num2str(states(h)));       
        for i = 1:Nfiles % Loop around Physical Data Files           
            file_label = physics{i};            
            for j = 1:Npartitions % Loop around Partitions                   
                partition_label_numerator = numerator{j};
                partition_label_denominator = denominator{j};
                if strcmp(numerator{j},'max') == 1
                    ratio_label = strcat(partition_label_numerator,'_',partition_label_denominator);
                    ratios.(state_label).(file_label).(ratio_label) = ele.(state_label).(partition_label_numerator).(file_label)/ele.(state_label).(partition_label_denominator).(file_label).mean;
                elseif strcmp(denominator{j},'max') == 1
                    ratio_label = strcat(partition_label_numerator,'_',partition_label_denominator);
                    ratios.(state_label).(file_label).(ratio_label) = ele.(state_label).(partition_label_numerator).(file_label).mean/ele.(state_label).(partition_label_denominator).(file_label);
                else
                    ratio_label = strcat(partition_label_numerator,'_',partition_label_denominator);
                    ratios.(state_label).(file_label).(ratio_label) = ele.(state_label).(partition_label_numerator).(file_label).mean/ele.(state_label).(partition_label_denominator).(file_label).mean;
                end % End of 'max' partition Conditional Loop
            end % End of Partitions Loop               
        end % End of Physical Data Files Loop
    end % End of Simulation States Loop    
end % End of ROI Ratios Function
