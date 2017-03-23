% =========================================================================
%
% datasum.m
%
% Data Summary
%
% Build to calculate the mean, std, and se of the physical values measured
% from the target mesh, using objective partitioning.
%
% Fluvio Lobo Fenoglietto
%
% =========================================================================

function [ele] = datasum(ele, partitions, states, files)
% Length of input arrays 
Nstates = length(states);
Npartitions = length(partitions);
Nfiles = length(files);
% The program consists of three (3) nested loops:
    for h = 1:Nstates % Loops around Simulation States
        state_label = strcat('state',num2str(states(h,1)));
        for i = 1:Npartitions % Loops around Partitions         
            partition_label = partitions{i};        
            for j = 1:Nfiles % Loop around Physiccal Data Files
                file_label = files{j};
                ele.(state_label).(partition_label).(file_label).raw = ele.(state_label).(partition_label).(file_label);
                ele.(state_label).(partition_label).(file_label).mean = mean(ele.(state_label).(partition_label).(file_label).raw(:,2));
                ele.(state_label).(partition_label).(file_label).std = std(ele.(state_label).(partition_label).(file_label).raw(:,2));
                ele.(state_label).(partition_label).(file_label).se = ele.(state_label).(partition_label).(file_label).std/length(ele.(state_label).(partition_label).(file_label).raw);
            end % End of Physical Data Files Loop         
        end % End of Partitions Loop
    end % End of Simulation States Loop
end % End of 'datasum.m' function
