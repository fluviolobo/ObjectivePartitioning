% =========================================================================
%
% objPart.m
%
% Objective Partitioning
%
% The following function uses the mesh info. structure "ele" and using the
% user-specified ROIs or objective partitions, determines the physical
% propertis in these regions within the target mesh
%
% Fluvio L. Lobo Fenoglietto
%
% =========================================================================

function [ele, ops] = objPart()

    % [1] Inputs:

    % [1.1] Importing 'ele' structure array
    [matfilename, matpathname] = uigetfile('*.mat','Select .mat file');
    matfilepath = fullfile(matpathname,matfilename);
    load(matfilepath)
    ele.matpathname = matpathname;        

    % [1.1.1] Structure verification
    %         Here the program verifies that the input structure
    %         has not been previously processed by objPart

    if isfield(ele,'partitions') == 1
        clc;
        disp(horzcat('The .mat file ',matfilename,' has already been processed through objPart'));
        reply1 = input(horzcat('Do you wish to re-process ',matfilename,' ? [y/n]'),'s');
        if strcmp(reply1,'y') == 1
            clc;
            disp(horzcat('User must re-execute "elementinfo.m"'));
            reply2 = input(horzcat('Do you wish to execute "elementinfo.m" directly ? [y/n]'),'s');
            if strcmp(reply2,'y') == 1
                disp(horzcat('Executing "elementinfo.m"...'));
                [ele] = elementinfo();
                ele.matpathname = matpathname;
                flag = 1;
            elseif strcmp(reply2,'n') == 1
                disp(horzcat('Exiting program...'));
                flag = 0;
            end
        elseif strcmp(reply1,'n') == 1
            disp(horzcat('Exiting program...'));
            flag = 0;
        end 
    elseif isfield(ele,'partitions') == 0
        flag = 1;
    end
    
    if flag == 1;
      
        % [1.2] Importing "xls" input file
        [xlsfilename, xlspathname] = uigetfile('*.xls','Select .xls file');
        xlsfilepath = fullfile(xlspathname,xlsfilename);

        % [1.2.1] Extracting data from '.xls' file
        % [1.2.1.1] Models
        [~, ~, raw] = xlsread(xlsfilepath,'Partitions');
        modellist = raw(:,1);
        for i = 1:length(modellist)   
            if strcmp(modellist{i,1},ele.structtitle) == 1       
                modelindex = i;
                break     
            end  
        end

        % [1.2.1.2] Objective Partitions or ROIs
        dimraw = size(raw);
        partitions = raw(3,3:dimraw(1,2));
        Npartitions = length(partitions);
        ele.partitions = partitions;
        R = cell2mat(raw(modelindex,3:dimraw(1,2)));
        origin = cell2mat(raw(modelindex+1:modelindex+3,3:dimraw(1,2)));     

        % [1.2.1.3] Simulation States
        %           Simplified list of simulation states or timepoints
        %           for analysis and visualization.
        [~, ~, raw] = xlsread(xlsfilepath,'Simulation States');
        simpstates = cell2mat(raw(2:end,1));

        % [1.2.1.4] Physical Data File
        %           Simplified list of physical data files for analysis
        [~, ~, raw] = xlsread(xlsfilepath,'Physics');
        files = raw(2:end,1);

        % [2] Processing
        simstate = ele.simstate;
        Nstates = length(simstate);

        for h = 1:Npartitions

            ops.id{h} = partitions{h};
            ops.(partitions{h}).R = R(h);
            ops.(partitions{h}).origin = ones(Nstates,3);
            for i = 1:3
                ops.(partitions{h}).origin(:,i) = origin(i,h).*ops.(partitions{h}).origin(:,i);
            end

            % [2.1] Partition or ROI migration
            [ele, ops] = movingorigin(ele, partitions(h), ops);

            % [2.2] Extracting or Segmenting ROI data
            [ele] = roidata(ele, partitions(h), simpstates, files);

            % [2.3] Simple statistics (Mean, SD, SE) on given physical
            % parameters, at specific simulation states.
            [ele] = datasum(ele, partitions(h), simpstates, files);
            
            % [2.4] Calculating the maximum value of a given physical
            % parameter, at specific simulation states.
            [ele] = elemax(ele, simpstates, files);

        end % End of 'partitions' loop

        [ele] = simstateplot(ele, ops, simpstates);

        % [3] Saving structures
        clearvars -except ele ops
        save(fullfile(ele.matpathname,strcat(ele.structtitle,'.mat')));
        
    elseif flag == 0;
        
        disp(horzcat('Program terminated'));
        
    end % End of conditional execution

end % End of objPart

