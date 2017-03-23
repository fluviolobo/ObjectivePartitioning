% =========================================================================
%
% elementinfo.m
%
% Element Information
%
% The following function extracts was built with the purpose of extracting
% the coordinates for every node defining every element comprising the
% target volumetric mesh.
%
% Fluvio L Lobo Fenoglietto
%
% =========================================================================

function [ele] = elementinfo()
    % Output file identification
    % The user must asign the name of the output structure file
    titledlg = inputdlg('Name for output structure of the FEA data file',...
                        'Output Structure Name', [1 50]);
    structtitle = titledlg{:};     
    % The, the program requests the -ascii output file from PostView, that
    % contains the simulation results.
    [filename, pathname, ~] = uigetfile('*','Select PostView -ascii output file','MultiSelect','on');
    ele.filename = filename; % Saving the names of each data file (reference to the physical property)    
    if ischar(filename) == 1   
        Nfiles = 1;
        mode = 1;
    elseif ischar(filename) == 0
        Nfiles = length(filename);
        mode = 2;
    end   
    for h = 1:Nfiles
        
        if mode == 1
            filepath = fullfile(pathname,filename);
            fileID = fopen(filepath);
            filenum = filename;
        elseif mode == 2
            filepath{h,1} = fullfile(pathname,filename{1,h});
            fileID = fopen(filepath{h,1});
            filenum = strcat(filename{1,h});
        end 
        
        disp(horzcat('DATA READ :: ',filenum));

        % The scanning of the -ascii extension is completed through a
        % while-loop. As long as "line" is made of "char", the while loop will
        % force the program to read the -ascii extension.
        %
        % The scanning of the -ascii ends when the program reads the "*STATE #"
        % section of the file.

        iter0 = 1; % Program iteration
        iter1 = 1;
        iter2 = 1;

        line = 'init'; % Initialize "line" as a string for the "while-loop"
                       % evaluation

        % Flags - Logicals
        state_flag = 0;
        node_coord_flag = 0;
        element_ref_flag = 0;
        element_data_flag = 0;

        while ischar(line) == 1

            line = fgetl(fileID);

            % The -ascii output extension from PostView has several headers
            % that repeat on every simulation time point (step). This program
            % reads and displays the headers in the MATLAB command window to
            % show the progress of the program.

            if strfind(line,'*ASCII SCENE EXPORT') > 0

                disp('HEADER READ')

            elseif strfind(line,'*STATE') > 0

                state_flag = 1; % Identify a line with reference to a simulation state
                state_label = strrep(strcat('state',line(7:end)),' ',''); % Labeling reference to such simulation state
                ele.simstate(iter1,1) = str2double(line(7:end)); % Store the number referencing the simulation state

                node_coord_flag = 0;
                element_ref_flag = 0;
                element_data_flag = 0;

                disp(horzcat('Reading STATE = ',strrep(line(7:end),' ','')))

            elseif strfind(line,'*TIME_VALUE') > 0

                ele.simstate(iter1,2) = str2double(line(12:end)); % Store the number referencing the simulation state

                node_coord_flag = 0;
                element_ref_flag = 0;
                element_data_flag = 0; 

                iter1 = iter1 + 1; % Updating "iter1" counter

            elseif strfind(line,'*NODES') > 0

                if state_flag == 0

    %                 state_label = 'state0'; % Referencing the initial configuration or initial state
    %                 ele.simstate(iter1,1) = 0; % 0th state
    %                 ele.simstate(iter1,2) = 0; % 0 sec.
    %                 
    %                 iter1 = iter1 + 1; % Updating "iter1" counter
    %                 
    %                 node_coord_flag = 1;
    %                 element_ref_flag = 0;
    %                 element_data_flag = 0;
    %                 
    %                 disp('Reading STATE = 0');
                    disp('Skipping STATE = 0');

                elseif state_flag ~= 0

                    node_coord_flag = 1;
                    element_ref_flag = 0;
                    element_data_flag = 0;

                    iter2 = 1; % Reset iteration counter

                end

            elseif strfind(line,'*ELEMENTS') > 0

                node_coord_flag = 0;
                element_ref_flag = 1;
                element_data_flag = 0;

                iter2 = 1; % Reset iteration counter

            elseif strfind(line,'*ELEMENT_DATA') > 0

                node_coord_flag = 0;
                element_ref_flag = 0;
                element_data_flag = 1;

                iter2 = 1; % Reset iteration counter

            end

            if isnan(str2double(line(end))) == 0

                if h == 1 && node_coord_flag == 1

                    index = strfind(line,',');
                    ele.(state_label).nodes(iter2,1) = str2double(line(1:index(1)-1));
                    ele.(state_label).nodes(iter2,2) = str2double(line(index(1)+1:index(2)-1));
                    ele.(state_label).nodes(iter2,3) = str2double(line(index(2)+1:index(3)-1));
                    ele.(state_label).nodes(iter2,4) = str2double(line(index(3)+1:end));

                    iter2 = iter2 + 1;

                elseif h == 1 && element_ref_flag == 1

                    index = strfind(line,',');
                    ele.elementref(iter2,1) = str2double(line(1:index(1)-1));
                    ele.elementref(iter2,2) = str2double(line(index(1)+1:index(2)-1));
                    ele.elementref(iter2,3) = str2double(line(index(2)+1:index(3)-1));
                    ele.elementref(iter2,4) = str2double(line(index(3)+1:index(4)-1));
                    ele.elementref(iter2,5) = str2double(line(index(4)+1:index(5)-1));
                    ele.elementref(iter2,6) = str2double(line(index(5)+1:index(6)-1));
                    ele.elementref(iter2,7) = str2double(line(index(6)+1:index(7)-1));
                    ele.elementref(iter2,8) = str2double(line(index(7)+1:index(8)-1));
                    ele.elementref(iter2,9) = str2double(line(index(8)+1:end));

                    iter2 = iter2 + 1;

                elseif element_data_flag == 1

                    index = strfind(line,',');
                    ele.(state_label).(filenum)(iter2,1) = str2double(line(1:index(1)-1));
                    ele.(state_label).(filenum)(iter2,2) = str2double(line(index(1)+1:end));

                    iter2 = iter2 + 1;

                end % End-of-Numeric-Check

            end % End-of-String-Check

            iter0 = iter0 + 1;

        end % End-of-While-Loop

        disp('DATA READ COMPLETE')
    
    end % End of multiple file selection   
    % Determining the centroids for every element,
    [ele] = elementcentroid(ele);    
    % Saving 'ele' structure
    ele.structtitle = structtitle;
    save(fullfile(pathname,strcat(structtitle,'.mat')));  
end % End-of-function