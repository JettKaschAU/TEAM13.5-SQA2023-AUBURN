import scanner
import parser
import constants
# Tests to see if isValidUserName will recognize an empty string
def isValidUserNameFuzzer(uName):
   for uName = "" 
   try:
      res = scanner.isValidUserNameFuzzer(uName)
   return res
   
# Tests to see if isValidPassword will recognoze an empty string      
def isValidPasswordFuzzer(pName):
   for pName = ""
   try:
      res = scanner.isValidPassword(pName)
   return res

# Tests to see if isValidKey will recognize an empty string
def isValidKeyFuzzer(keyName):
   for keyName = ""
   try:
      res = scanner.isValidKey(keyName)
   return res
   
# Tests to make sure checkIfWeirdYAML will skip invalid YAMLs
def  checkIfWeirdYAMLFuzzer(yaml_script):
   for yaml_script = "./github/workflows/"
   try:
      res = parser.checkIfWeirdYAML(yaml_script)
   return res
   
# Tests to make sure scanPasswords blocks incorrect passwords
def scanPasswordsFuzzer(k_, val_lis):
   for k_ = "passwords"
   try:
      res = scanner.scanPasswords(k_, val_lis)
   return res
   
if __name__=='__main__':
    isValidUserNameFuzzer()
    isValidPasswordFuzzer()
    isValidKeyFuzzer()
    checkIfWeirdYAMLFuzzer()
    scanPasswordsFuzzer()