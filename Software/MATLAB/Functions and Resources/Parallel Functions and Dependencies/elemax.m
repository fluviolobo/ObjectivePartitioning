%
% elemax.m
%
% Project: Objective Partitioning
%
% Description: Determnes the maximum value of an input physical quantity 
% within a mesh
%
% Author: Fluvio Lobo Fenoglietto
%

function [ele] = elemax(ele,states,physics)
    Nstates = length(states);
    Nfiles = length(physics);    
    for h = 1:Nstates % Loop around Simulation States    
        state_label = strcat('state',num2str(states(h)));        
        for i = 1:Nfiles % Loop around Physical Data Files          
            file_label = physics{i};            
            ele.(state_label).max.(file_label) = max(ele.(state_label).(file_label)(:,2));           
        end % End of Physical Data Files Loop
    end % End of Simulation States Loop
end % End of 'elemax' function

