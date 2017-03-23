% =========================================================================
%
% movingorigin.m
%
% // Moving Origin //
%
% Given that the nodal displacement of irregular geometries and
% non-homogenous materials is not uniform, the following code is used to
% approximate the position of the origin of an objective partition
% throughout the materials deformation.
%
% Fluvio L Lobo Fenoglietto
% lobox015@umn.edu
%
% =========================================================================

function [ele, ops] = movingorigin(ele, partitions, ops)

    % Importing element info
    simstate = ele.simstate;
    
    Nstates = length(simstate);
    Npartitions = length(partitions);
    
    for h = 1:Npartitions
        
        h
        
        partition_label = partitions{h};

        for i = 1:Nstates

        state_label = strcat('state',num2str(simstate(i)));

        % Optimization loop
        maxerror = 1;
        tol = 0.0001;
        optiter = 1;

        disp(horzcat('Optimizing OP-origin for STATE = ',num2str(simstate(i))));

            while maxerror > tol

                % Selection of elements and extraction of data using input sphere origin
                [ele] = elementselection(ele, partitions(h), simstate(i,1), ops);
                [ele] = roidata(ele, partitions(h), simstate(i,1), {'dispx','dispy','dispz'});

                origin_guess = ops.(partition_label).origin(i,:);

                % Updating origin based on displacement vectors

                dx = mean(ele.(state_label).(partition_label).dispx(:,2));
                dy = mean(ele.(state_label).(partition_label).dispy(:,2));
                dz = mean(ele.(state_label).(partition_label).dispz(:,2));

                ops.(partition_label).origin(i,:) = [ops.(partition_label).origin(1,1) + dx, ...
                                                  ops.(partition_label).origin(1,2) + dy, ...
                                                  ops.(partition_label).origin(1,3) + dz];

                origin_update = ops.(partition_label).origin(i,:);

                [ele] = elementselection(ele, partitions(h), simstate(i,1), ops);
                [ele] = roidata(ele, partitions(h), simstate(i,1), {'dispx','dispy','dispz'});

                error = [(origin_update(1)-origin_guess(1))^2, ...
                         (origin_update(2)-origin_guess(2))^2, ...
                         (origin_update(3)-origin_guess(3))^2];

                maxerror = max(error);
                optiter = optiter + 1;

            end % End of while loop

            ops.(partition_label).origin(i+1,:) = ops.(partition_label).origin(i,:);

            disp(horzcat('Optimization Complete ERROR = ',num2str(maxerror)));

            ops.(partition_label).optsum(i,:) = [i, optiter, maxerror]; % Optimization Summary

        end % End of Sim. State Loop
        
    end % End of Partitions Loop

end % End of function





