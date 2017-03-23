% =========================================================================
%
% elementcentroid.m
%
% // Element Centroid //
%
% Given that certain physical properties are associated with the entirety
% of an element (e.g. stress), rather than the nodes that compose them
% (e.g. displacements), this program has been built with the purpose of
% calculating a geometric centroid for every element of a target mesh.
%
% The program takes the following inputs:
%
% 1- ele [struc] : Structure array containing nodal and element data for
%                  every simulation state (time point).
%
% Fluvio L Lobo Fenoglietto
% lobox015@umn.edu
%
% =========================================================================

function [ele] = elementcentroid(ele)   
    disp('CENTROID CALCULATION');
    % Importing data from structure array
    simstate = ele.simstate;
    elementsref = ele.elementref;
    
    Nstates = length(simstate);
    for h = 1:Nstates
        disp(horzcat('Centroid Calculation for STATE = ',num2str(simstate(h))));
        state_label = strcat('state',num2str(simstate(h)));
        ele.(state_label).elementcoord(:,1) = elementsref(:,1);
        dim = size(elementsref);
        for i = 1:dim(1)      
            element_nodes = zeros(dim(2)-1,3);     
            for j = 2:dim(2)        
                node = elementsref(i,j); % Pick one of the nodes that composes the element being studied!
                node_id = ele.(state_label).nodes(:,1)==node; % Determining the "id" of that node within the list of al "nodes".
                element_nodes(j-1,:) = ele.(state_label).nodes(node_id,2:end);      
            end
%           disp(horzcat('Element = ',num2str(i),'/',num2str(dim(1))));
            ele.(state_label).elementcoord(i,2:4) = [mean(element_nodes(:,1)), mean(element_nodes(:,2)), mean(element_nodes(:,3))];  
%           plot3(element_nodes(:,1),element_nodes(:,2),element_nodes(:,3),'ko'); grid on; hold on;
%           plot3(element_coord(i,2),element_coord(i,3),element_coord(i,4),'r*');
%           xlabel('X'); ylabel('Y'); zlabel('Z');
        end
    end
    disp('CENTROID CALCULATION COMPLETED');
end