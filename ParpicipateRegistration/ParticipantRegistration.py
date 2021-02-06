ParticipantList=[["NAME |","COUNTRY |","AGE"]]
OutputList=open("Participant_sList.txt","w")
ParticipantNumber=5
Participant=0
while(Participant<ParticipantNumber):
    ParticipantInformation = [ ]
    ParticipantInformation.append(input("Pls write your Name: "))
    ParticipantInformation.append(input("Pls write your Country: "))
    ParticipantInformation.append(input("Pls write your age: "))
    Participant+=1
    ParticipantList.append(ParticipantInformation)
    print(ParticipantInformation)
for ParticipantInformation in ParticipantList:
    for Participant in ParticipantInformation:
        OutputList.write(Participant)
        OutputList.write(" |")
    OutputList.write("\n")
OutputList.close()
