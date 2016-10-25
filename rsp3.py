"""
========================
  Rock Scissors Paper
========================

1. Creator : GeonHee Han
2. Date : 2016 . 10 .12

"""

import random


def main() :

    """
    This function is Rock Scissors Paper game
        between user and computer 10 time
    - com : randomly chose one in (Rock, Scissors, Paper)
    - player : user choose one shape
    - return : each time print you win , lose or draw

    """
    print("가위바위보 세계에 오신것을 환영합니다. ")
    name = str(input("플레이어의 이름을 입력해주세요. : "))
    one = 'y'
    game, draw ,win, lose = 0, 0, 0, 0
    while (one == 'y') or (one == "Y") :
        for i in range(10):
            com = random.randrange(1,4)
            player = int(input("가위~ 바위 보! 바위(1) 가위(2) 보(3) "))
            while not (player == 1 or player == 2 or player ==3):
                player = int(input("다시 내!\n 가위~ 바위 보! 바위(1) 가위(2) 보(3) "))

            if (player == 1):
                if (com == 1):
                    print("컴퓨터는 바위를 냈어요. 아쉽게 비겼네요...")
                    draw += 1

                elif (com ==2 ):
                    print("컴퓨터는 가위를 냈어요. 축하해요!! 당신이 이겼어요!!")
                    win += 1
                else :
                    print("컴퓨터는 보자기를 냈어요. 졌네요.. 괜찮아요 다음에 이기면 되죠!")
                    lose += 1
            elif (player == 2):
                if (player == 1):
                    print("컴퓨터는 바위를 냈어요. 졌네요.. 괜찮아요 다음에 이기면 되죠!")
                    lose +=1
                elif (player ==2 ):
                    print("컴퓨터는 가위를 냈어요. 아쉽게 비겼네요...")
                    draw +=1
                else :
                    print("컴퓨터는 보자기를 냈어요. 축하해요!! 당신이 이겼어요!!")
                    win += 1
            else:
                if (player == 1):
                    print("컴퓨터는 바위를 냈어요. 축하해요!! 당신이 이겼어요!!")
                    win += 1
                elif (player ==2 ):
                    print("컴퓨터는 가위를 냈어요. 졌네요.. 괜찮아요 다음에 이기면 되죠!")
                    lose += 1
                else :
                    print("컴퓨터는 보자기를 냈어요. 아쉽게 비겼네요...")
                    draw +=1
        game += 1
        print (name + "님의 전적은 " + game*10 + "전")
        print (str(win) + "승 "+ str(draw)+ "무 " + str(lose) + "패 입니다.")
        one = str(input("한번더 하시겠습니까? (y/n)"))
main()
