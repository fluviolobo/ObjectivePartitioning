% =========================================================================
%
% elementselection.m
%
% // Element Selection //
%
% Provided the coordinates of a region of interest (ROI) and the centroidal
% coordinates of all the elements of a taget volumetric mesh, this function
% determines which elements of the target mesh fall within the ROI.
%
% The program takes the following inputs:
% 1- element_coord (nx4 matrix): matrix containing the list of elements (n
%                                rows) on the first column, followed by
%                                their corresponding coordinates in 3D
%                                space (2:4 columns [x,y,z]).
% 2- roi_coord (meshgrids): 3 matrices, one per cartesian coordinate. This
%                           is the common output of surface meshes in
%                           MATLAB.
%
% Fluvio L Lobo Fenoglietto
% lobox015@umn.edu
%
% =========================================================================

function [ele] = elementselection(ele, partitions, states, ops)
    Npartitions = length(partitions);
    Nstates = length(states);
    for h = 1:Npartitions
        for i = 1:Nstates
            partition_label = partitions{h}; 
            partition_centroid = ops.(partition_label).origin(states(i),:);
            R = ops.(partition_label).R;           
            state_label = strcat('state',num2str(states(i)));
            element_coord = ele.(state_label).elementcoord;
            dim = size(element_coord);
            % First, the program calculates the distance of all the element
            % centroids to the origin of the ROI.
            roi_diff = zeros(dim(1),2);
            roi_diff(:,1) = element_coord(:,1);
            j = 1; % External counter
            for k = 1:dim(1)
                roi_diff(k,2) = sqrt((element_coord(k,2)-partition_centroid(1))^2 + ...
                                     (element_coord(k,3)-partition_centroid(2))^2 + ...
                                     (element_coord(k,4)-partition_centroid(3))^2);
                if roi_diff(k,2) < R
                    ele.(state_label).(partition_label).list(j,1) = roi_diff(k,1); % Element number (code)
                    ele.(state_label).(partition_label).list(j,2) = roi_diff(k,1)-1; % Element number (visual)
                    j = j + 1;
                end % End of ROI discrimination
            end % End of Element Coord. Loop
        end % End of Sim. States Loop
    end % End of Partitions Loop
end
    
 