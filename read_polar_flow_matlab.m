clear all
close all
clc

fname = 'training-session-2021-02-28-1116.json';
val = jsondecode(fileread(fname));

range = length(val.exercises.samples.speed);
speed_var_no_zeros = [];

for i = 1:range
    try 
        speed_var(i) = val.exercises.samples.speed{i}.value;
    catch error 
        disp(['value ' num2str(i) ' does not exist']);        
    end
end

%%
for i = 1:range
    if speed_var(i) ~= 0
        speed_var_no_zeros = [speed_var_no_zeros speed_var(i)]; 
    end
end

