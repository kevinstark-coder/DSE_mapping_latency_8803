import subprocess
from configparser import ConfigParser
import pandas as pd
def modify_cfg_file(cfg_file_path, new_values):
#     """
#     Modify specific variables in a cfg file using the configparser module.
#     """
    config = ConfigParser()
    config.read(cfg_file_path)
    
    for section in config.sections():
        for key, value in new_values.items():
            if key in config[section]:
                config.set(section, key, str(value))
    
    with open(cfg_file_path, 'w') as file:
        config.write(file)

def run_shell_command(command):
#     """
#     Run a shell command using subprocess.run and return the CompletedProcess instance.
#     """
    return subprocess.run(command, capture_output=True, text=True)

# # Define the path to your configuration file
cfg_file_path = './system.cfg'

# # Define the shell command you want to run
shell_command_gemm = [
    "python", "./scale-sim-v2/scalesim/scale.py", 
    "-c", "./system.cfg", 
    "-t", "./lenet_conv.csv", 
    # "-t", "./conv_test.csv", 
    "-i", "gemm", 
    "-p", "./DSE_output_gemm"
]

shell_command_conv = [
    "python", "./scale-sim-v2/scalesim/scale.py", 
    "-c", "./system.cfg", 
    # "-t", "./lenet_conv.csv", 
    "-t", "./conv_test.csv", 
    "-p", "./DSE_output_conv"
]

# # Define the different configurations you want to use
configurations = {'ArrayHeight': '1', 'ArrayWidth': '1', 'IfmapSramSzkB': '1', 'FilterSramSzkB': '1', 'OfmapSramSzkB': '1', 'Dataflow': 'ws','bandwidth':'1'}
#     # Add more configurations as needed

dataflow = ["ws","os","is"]
# Loop through each configuration, update the cfg file, and run the shell command
#---------------------------------------------------------------A1.1-----------------------------------------------

# configurations['ArrayHeight'] = 3
# configurations['ArrayWidth'] = 6
# configurations['IfmapSramSzkB'] = 1
# configurations['FilterSramSzkB'] = 1
# configurations["OfmapSramSzkB"] = 1
# configurations["Dataflow"] = "os"
# modify_cfg_file(cfg_file_path, configurations)
# result = run_shell_command(shell_command_conv)
# # Check the result of the shell command
# if result.returncode == 0:
#     print("conv Command succeeded---------------------------------------------------")
# else:
#     print("Command failed with errors:")
#     print(result.stderr)
# result = run_shell_command(shell_command_gemm)
# # Check the result of the shell command
# if result.returncode == 0:
#     print("gemm Command succeeded---------------------------------------------------")
# else:
#     print("Command failed with errors:")
#     print(result.stderr)
# df_conv = pd.read_csv("./DSE_output_conv/lenet_DSE_run/COMPUTE_REPORT.csv")
# df_gemm = pd.read_csv("./DSE_output_gemm/lenet_DSE_run/COMPUTE_REPORT.csv")
# df_new = pd.concat([df_conv,df_gemm],ignore_index = True)
# # print(df_new[" Total Cycles"].mean())
# # print(df_new[" Mapping Efficiency %"].mean())
# print(df_new[" Total Cycles"].sum())
# total_area = 525 * 21 + 1015.7 * 3* 1
# print(total_area)

#---------------------------------------------------------------A1.2-----------------------------------------------
'''
def searchpara():
    for i in range(3,11):
        for j in range(3,11):
            for k in range(1,5):
                for l in range(1,5):
                    for m in range(1,5):
                        for n in dataflow:
                            configurations['ArrayHeight'] = i
                            configurations['ArrayWidth'] = j
                            configurations['IfmapSramSzkB'] = k
                            configurations['FilterSramSzkB'] = l
                            configurations["OfmapSramSzkB"] = m
                            configurations["Dataflow"] = n
                            modify_cfg_file(cfg_file_path, configurations)
                            result = run_shell_command(shell_command_conv)
                            # Check the result of the shell command
                            if result.returncode == 0:
                                print("conv Command succeeded---------------------------------------------------")
                            else:
                                print("Command failed with errors:")
                                print(result.stderr)
                            result = run_shell_command(shell_command_gemm)
                            # Check the result of the shell command
                            if result.returncode == 0:
                                print("gemm Command succeeded---------------------------------------------------")
                            else:
                                print("Command failed with errors:")
                                print(result.stderr)
                            df_conv = pd.read_csv("./DSE_output_conv/lenet_DSE_run/COMPUTE_REPORT.csv")
                            df_gemm = pd.read_csv("./DSE_output_gemm/lenet_DSE_run/COMPUTE_REPORT.csv")
                            df_new = pd.concat([df_conv,df_gemm],ignore_index = True)
                            print(df_new[" Total Cycles"].mean())
                            print(df_new[" Mapping Efficiency %"].mean())
                            if((df_new[" Total Cycles"].mean()<10**4) and (df_new[" Mapping Efficiency %"].mean()>90)):
                                return i,j,k,l,m,n

i,j,k,l,m,n = searchpara()
with open ("log.txt","w") as file:
    file.writelines(f"ArrayHeight {i} \nArrayWidth {j} \nIfmapSramSzkB {k} \nFilterSramSzkB {l} OfmapSramSzkB {m} \nDataflow {n}  ")
print('ArrayHeight   ',i, '\nArrayWidth  ', j, '\nIfmapSramSzkB   ', k, '\nFilterSramSzkB   ',l, \
      'OfmapSramSzkB',m, '\nDataflow',n)

'''

'''
#---------------------------------------------------------------A1.3-----------------------------------------------
import matplotlib.pyplot as plt
def searchpara():
    for k in range(1,4):
        plt.figure()
        plt.title(f"SRAM {k}B plot")
        plt.xlabel("MAC units")
        plt.ylabel("Total Cycles" )
        plt.grid(True)
        for n in dataflow:
            x=[]
            y=[]
            dic={}
            for i in range(3,11):
                for j in range(3,11):
                    configurations['ArrayHeight'] = i
                    configurations['ArrayWidth'] = j
                    configurations['IfmapSramSzkB'] = k
                    configurations['FilterSramSzkB'] = k
                    configurations["OfmapSramSzkB"] = k
                    configurations["Dataflow"] = n
                    modify_cfg_file(cfg_file_path, configurations)
                    result = run_shell_command(shell_command_conv)
                    # Check the result of the shell command
                    if result.returncode == 0:
                        print("conv Command succeeded---------------------------------------------------")
                    else:
                        print("Command failed with errors:")
                        print(result.stderr)
                    result = run_shell_command(shell_command_gemm)
                    # Check the result of the shell command
                    if result.returncode == 0:
                        print("gemm Command succeeded---------------------------------------------------")
                    else:
                        print("Command failed with errors:")
                        print(result.stderr)
                    df_conv = pd.read_csv("./DSE_output_conv/lenet_DSE_run/COMPUTE_REPORT.csv")
                    df_gemm = pd.read_csv("./DSE_output_gemm/lenet_DSE_run/COMPUTE_REPORT.csv")
                    df_new = pd.concat([df_conv,df_gemm],ignore_index = True)
                    sum = df_new[" Total Cycles"].sum()
                    total_area = 525 * i*j + 1015.7 * 3* k
                    print(f"sum is {sum}, total_area is {total_area}" )
                    #compare the constraint
                    if((sum<17500) and (total_area<15000)):
                        with open ("log.txt","a") as file:
                            file.writelines(f"ArrayHeight {i} \nArrayWidth {j} \nIfmapSramSzkB {k} \nFilterSramSzkB {k} OfmapSramSzkB {k} \nDataflow {n}  ")
                    #draw the graph
                    num_pe = i*j
                    if num_pe in dic:
                        dic[num_pe] = sum if sum<dic[num_pe] else dic[num_pe]
                    else:
                        dic[num_pe] = sum

            for key in dic:
                x.append(key)
                y.append(dic[key])
            plt.scatter(x,y,label=f'{n}')
            plt.legend()
            print(f'the {k} kB SRAM in {n} mode accomplished')
        plt.savefig(f'{k}kB_SRAM.png')
        
i,j,k,n = searchpara()
'''
#---------------------------------------------------------------B1-----------------------------------------------
'''
def searchpara():

    for k in range(5,11):
        for l in range(5,11):
            for m in range(5,11):
                for i in range(5,11):
                    for j in range(2,11):
                    
                        # for n in dataflow:
                            for p in range(5,6):
                                configurations['ArrayHeight'] = i
                                configurations['ArrayWidth'] = j
                                configurations['IfmapSramSzkB'] = k
                                configurations['FilterSramSzkB'] = l
                                configurations["OfmapSramSzkB"] = m
                                configurations["Dataflow"] = 'ws'
                                configurations["bandwidth"] = p
                                modify_cfg_file(cfg_file_path, configurations)
                                result = run_shell_command(shell_command_conv)
                                # Check the result of the shell command
                                if result.returncode == 0:
                                    print("conv Command succeeded---------------------------------------------------")
                                else:
                                    print("Command failed with errors:")
                                    print(result.stderr)
                                result = run_shell_command(shell_command_gemm)
                                # Check the result of the shell command
                                if result.returncode == 0:
                                    print("gemm Command succeeded---------------------------------------------------")
                                else:
                                    print("Command failed with errors:")
                                    print(result.stderr)
                                df_conv = pd.read_csv("./DSE_output_conv/lenet_DSE_run/COMPUTE_REPORT.csv")
                                df_gemm = pd.read_csv("./DSE_output_gemm/lenet_DSE_run/COMPUTE_REPORT.csv")
                                df_new = pd.concat([df_conv,df_gemm],ignore_index = True)
                                print(df_new[" Mapping Efficiency %"].mean())
                                print('ArrayHeight   ',i, '\nArrayWidth  ', j, '\nIfmapSramSzkB   ', k, '\nFilterSramSzkB   ',l, \
                                'OfmapSramSzkB   ',m, '\nDataflow   ','ws', '\nbandwidth   ',p)
                                if(df_new[" Mapping Efficiency %"].mean()>94):
                                    print('df_new[" Mapping Efficiency %"].mean()',"1111111111111")
                                    print(p,"2222")
                                    return i,j,k,l,m,'ws',p
    return None
if searchpara() == None:
    print("not valid")
else:
    i,j,k,l,m,n,p=searchpara()
    with open ("log.txt","w") as file:
        file.writelines(f"ArrayHeight {i} \nArrayWidth {j} \nIfmapSramSzkB {k} \nFilterSramSzkB {l} OfmapSramSzkB {m} \nDataflow {n} \m bandwidth {p}  ")
    print('ArrayHeight   ',i, '\nArrayWidth  ', j, '\nIfmapSramSzkB   ', k, '\nFilterSramSzkB   ',l, \
        'OfmapSramSzkB   ',m, '\nDataflow   ',n, '\nbandwidth   ',p)

'''
#---------------------------------------------------------------B1.2&1.3-----------------------------------------------
  
'''
configurations['ArrayHeight'] = 5
configurations['ArrayWidth'] = 2
configurations['IfmapSramSzkB'] = 1
configurations['FilterSramSzkB'] = 1
configurations["OfmapSramSzkB"] = 5
configurations["bandwidth"] = 5
configurations["Dataflow"] = "ws"
modify_cfg_file(cfg_file_path, configurations)
result = run_shell_command(shell_command_conv)
# Check the result of the shell command
if result.returncode == 0:
    print("conv Command succeeded---------------------------------------------------")
else:
    print("Command failed with errors:")
    print(result.stderr)
result = run_shell_command(shell_command_gemm)
# Check the result of the shell command
if result.returncode == 0:
    print("gemm Command succeeded---------------------------------------------------")
else:
    print("Command failed with errors:")
    print(result.stderr)
df_conv = pd.read_csv("./DSE_output_conv/lenet_DSE_run/BANDWIDTH_REPORT.csv")
df_gemm = pd.read_csv("./DSE_output_gemm/lenet_DSE_run/BANDWIDTH_REPORT.csv")
df_new1 = pd.concat([df_conv,df_gemm],ignore_index = True).values

df_conv = pd.read_csv("./DSE_output_conv/lenet_DSE_run/COMPUTE_REPORT.csv")
df_gemm = pd.read_csv("./DSE_output_gemm/lenet_DSE_run/COMPUTE_REPORT.csv")
df_new2 = pd.concat([df_conv,df_gemm],ignore_index = True).values

den = 0
nominator = 0
stall = 0
for i in range(0,5):
    
    nominator += (df_new1[i,4].astype(float)+df_new1[i,5].astype(float))/2 * df_new2[i,1].astype(float)
    # print(df_new1[i,1],"  ",df_new1[i,2],"  " ,df_new2[i,1])
    stall += df_new2[i,2]
    den += df_new2[i,1]
    # print(den," den ")

# print(df_new[" Total Cycles"].mean())
# print(df_new[" Mapping Efficiency %"].mean())
# print(nominator/den,"", stall, "", den)
        # print(total_area)
'''
#---------------------------------------------------------------B2-----------------------------------------------

configurations['ArrayHeight'] = 4
configurations['ArrayWidth'] = 4
configurations['IfmapSramSzkB'] = 10
configurations['FilterSramSzkB'] = 10
configurations["OfmapSramSzkB"] = 10
configurations["bandwidth"] = 10
configurations["Dataflow"] = "ws"
configurations["run_name"] = 'B_test'
modify_cfg_file(cfg_file_path, configurations)
result = run_shell_command(shell_command_conv)
# Check the result of the shell command
if result.returncode == 0:
    print("conv Command succeeded---------------------------------------------------")
else:
    print("Command failed with errors:")
    print(result.stderr)

df_conv = pd.read_csv("./DSE_output_conv/B_test/COMPUTE_REPORT.csv").values
print(df_conv[:,1])


