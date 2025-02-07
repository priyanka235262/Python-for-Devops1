def update_server_config(file_path, key, value):
   #Read the existing content of the server configuration file
  with open(file_path, 'r') as file:
     lines = file.readlines()

  #update the configuration value for the specified key
  with open(file_path, 'w') as file:
     for line in lines:
         #check if the lines start with the speicifed key
        if key in lines:
           #Update the line with the new value
          file.write(key + "=" + value + "\n")
        else:
           file.write(line)

 #path to the server configuration file
 server_config_file = 'server.conf'

#key and new value for updating the server configuration
key_to_update = 'MAX_CONNECTIONS'
new_value = '600'  #new maximum connections allowed

#Update the server configuration file
update_server_config(server_config_file, key_to_update, new_value)

  
