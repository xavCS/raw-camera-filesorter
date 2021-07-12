import os
import shutil
import time
import easygui

raw_formats = ['.CR2','.NRW','.EIP','.RAF','.ERF','.RW2','.RWZ','.ARW','.DNG','.NEF','.K25','.ARI','.SRF','.DCR',
'.RAW','.CRW','.BAY','.3FR','.CS1','.MEF','.ORF','.KDC','.MOS','.MFW','.SR2','.FFF','.CR3','.SRW','.RWL','.J6I','.KC2',
'.X3F','.MRW','.IIQ','.PEF','.CXI','.MDC'
]
#make a directory menu for the less tech savvy
path = easygui.diropenbox()

curr_dir = path #too lazy to change existing calls of this variable to 'path'
os.chdir(path)

users_files = os.listdir()


for extension in range(len(users_files)):
    if os.path.splitext(users_files[extension])[1] in raw_formats:
        raw_formatappend = [os.path.splitext(users_files[extension])[1]]


removed_extensions = [os.path.splitext(File)[0] for File in os.listdir()] ##for each file in the directory, strip its extension, then append index[0] to removed_extensions

uniques = {filename for filename in removed_extensions} #removing duplicates

for e in uniques:
    if e in removed_extensions:
        removed_extensions.remove(e)       

#universal file extensions implementation for different cameras
cleaned_selections = [removed_extensions[i]+raw_formatappend[0] for i in range(len(removed_extensions))]

try:
    os.makedirs('Client Choices')
except:
    print("FOLDER 'Client Choices' ALREADY EXISTS. SKIPPING FOLDER CREATION...") #nothing happens, folder already exists

comparison = os.listdir()

for i in range(len(comparison)):
    if comparison[i] in cleaned_selections:
        shutil.move(f'{curr_dir}/{comparison[i]}',f'{curr_dir}/Client Choices')

print('\n')

time.sleep(1.5)
if len(cleaned_selections) == 0:
    print("NO FILES TO TRANSFER. FILES ALREADY SORTED ON THIS FOLDER?\nCHECK RAW FILES.")
else:
    print("TRANSFER COMPLETE. QUITTING...")
time.sleep(1.5)
quit()
