import requests
from requests.auth import HTTPBasicAuth
import settings

def get_file_from_server(filename,time_now):

    req_url = "".join([settings.CERT_SERVER_BASE_URL,filename])
    req = requests.get(req_url,verify=False,auth=HTTPBasicAuth('foo','bar'))
    # print(req.status_code,req.reason,req.text)
    #If we get the file
    if(int(req.status_code) == 200):
        #Get response content(file)
        file = req.text
        #Save file to bakcup folder
        saved_file_name = "".join([filename,'-',time_now,'.bkp'])
        saved_file_name_abs = "".join([settings.BACKUP_FOLDER,saved_file_name])
        with open(saved_file_name_abs,'w') as f:
            f.write(file)
        log_msg = 'Download success. Download URL: %s, Status: %s, Saved to: %s' %(req_url,req.status_code,saved_file_name)
        settings.log_func.info(log_msg)
        #Return the file name and the file content
        return (saved_file_name,file)
    else:
        log_msg = 'Download failed. Download URL: %s, Status: %s' %(req_url,req.status_code)
        settings.log_func.error(log_msg)
        return (None,None)

if __name__ == '__main__':
    get_file_from_server('neweggsite_2018-03-27.key','201804031015')