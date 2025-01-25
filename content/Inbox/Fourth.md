# Questions/investigation

Going forward see:
C:\Users\RhysL\Desktop\Fourth\fourth\packages\artifacts_management\README.md

Investigate:
- packages/artifacts_management/artifacts_management
- packages/data_io_services/tests
- packages/timeseries_processing/tests
#### Potential issues to ask later
---
Data storage and access

What is the mechanism to handle storage of the user's csv? Do you compress it to tar.gz format for storage in the cloud?

Does it relate to:

fourth/packages/data_io_services

---
Run make file first:

Developer Testing

If developers want to test scripts would it be best to set up a workspace, or have requirements file for them to build local virtual environments? 

See: Main README and ### Repository Structure

Are you testing the application by running test scripts and checking that the dev enviroment is stable

#### Notes

Generic folder for [[Google Cloud Platform]] setup
Folder: fourth\gcp_project_setup 

dev is current branch

This project is managed in [[Gitlab]] which is used for [[standardised/CI-CD|CI-CD]]

The main terminal scripting is in bash (linux)? Not cmd,or powershel.