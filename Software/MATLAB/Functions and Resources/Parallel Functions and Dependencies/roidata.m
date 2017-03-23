% =========================================================================
%
% roidata.m
%
% Region of Interest (ROI) Data
%
% The function was designed to extract given physical data from the
% elements composing given mesh partitions, at specific simulation states
%
% Fluvio Lobo Fenoglietto
%
% =========================================================================

function [ele] = roidata(ele, partitions, states, files)
    % Length of input arrays
    Npartitions = length(partitions);
    Nstates = length(states);
    Nfiles = length(files);  
    for h = 1:Npartitions % Loop around partitions       
        partition_label = partitions{h};
        for i = 1:Nstates % Loop around Simulation States
            state_label = strcat('state',num2str(states(i)));
            for j = 1:Nfiles % Loop around Physical Data Files
                file_label = files{j};
                k = 1; % External counter
                partition_element_list = ele.(state_label).(partition_label).list(:,1);
                physics_element_list = ele.(state_label).(file_label)(:,1);
                Npartele = length(partition_element_list);
                for l = 1:Npartele % Loop around list of elements within partitions
                    roi_element = partition_element_list(l,1);
                    index = find(physics_element_list == roi_element);
                    if isempty(index) == 0
                        ele.(state_label).(partition_label).(file_label)(k,:) = ele.(state_label).(file_label)(index(1),:);
                        k = k + 1;
                    end 
                end % End of ROI Loop
            end % End of Physical Data Files Loop
        end % End of Simulation States Loop        
    end % End of Partitions Loop   
end % End of 'roidata.m' function