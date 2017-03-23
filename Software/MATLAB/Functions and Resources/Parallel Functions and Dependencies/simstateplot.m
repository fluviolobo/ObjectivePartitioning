% =========================================================================
%
% simstateplot.m
%
% Element Maximum
%
% Build to plot sections of the data for validation.
%
% Fluvio Lobo Fenoglietto
%
% =========================================================================

function [ele] = simstateplot(ele,sphere,plotstates)
    % Info. from structure array
    partitions = ele.partitions;
    % Length of input arrays 
    Nsimpstates = length(plotstates);
    Npartitions = length(partitions);
    for h = 1:Nsimpstates % Loop around simulation states
        state_label = strcat('state',num2str(plotstates(h)));
        disp('Plotting 2D (X-Y) view of model geometry')
        figure (h),
        for i = 1:length(ele.(state_label).elementcoord(:,1)) % Loop around Element Centroids
            if ele.(state_label).elementcoord(i,4) <= 1.5*min(ele.(state_label).elementcoord(:,4))
                plot(ele.(state_label).elementcoord(i,2),ele.(state_label).elementcoord(i,3),'r.')
                hold on
            end % End of Centroid Coordinate Conditional Statement
        end % End of Element Centroids Loop    
        for i = 1:Npartitions % Loop around partitions         
            partition_label = partitions{i};
            disp(horzcat('Plotting Partition #',num2str(i),'/',num2str(Npartitions)));
            circle.R = sphere.(partition_label).R;
            circle.origin = sphere.(partition_label).origin(plotstates(h),1:2);
            theta = 0:0.001:2*pi;      
            for j = 1:length(theta)
                circle.perim(j,:) = circle.R*[cos(theta(j)), sin(theta(j))] + circle.origin;
            end           
            plot(circle.perim(:,1),circle.perim(:,2),'b-','LineWidth',2)
            plot(circle.origin(1),circle.origin(2),'bo','LineWidth',2)
            hold on
            grid on
            % axis([-0.5 4 -0.5 2])
            xlabel('X (mm)')
            ylabel('Y (mm)')
            title(horzcat('STATE = ',num2str(plotstates(h))));           
        end % End of Partitions Loop
        saveas(gcf,strcat(ele.matpathname,state_label,'.png'));
    end % End of Simulation States Loop   
end % End of 'simpstateplot.m' function
