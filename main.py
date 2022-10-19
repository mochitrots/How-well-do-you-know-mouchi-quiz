def new_game():
	user_resp_list = []
	correct_usr_ans = 0
	opt_num = 0
	for key in questions:
		print("----------------")
		print(key)
		for i in options[opt_num]:
			print(i)
		
		usr_resp = input("Enter A, B, C or D: ").upper()
		user_resp_list.append(usr_resp)
		correct_usr_ans += check_ans(questions.get(key), usr_resp)
		opt_num += 1
	display_score(correct_usr_ans, user_resp_list)
		

def check_ans(answer, usr_resp):
	if answer == usr_resp:
		print("You're right!! You get +1 point")
		return 1
	else:
		print("You're wrong. You lose 0.25 points")
		return -0.25

def display_score(correct_usr_ans, user_resp_list):
	print()
	print("RESULTS:")
	print("Right answers: ", end="")
	for i in questions:
		print(questions.get(i), end=" ")
	print()

	print("Your responses: ", end="")
	for i in user_resp_list:
		print(i, end=" ")
	print()
	score = correct_usr_ans
	print("Your score is "+str(score))
	percent = (score/4)*100
	print("Your percentage is "+str(percent)+"%")

def play_again():
	pass


questions = {
    "What type of pokemon is mouuchii? ":"C",
    "What is mouuchii's favorite activity? ":"A",
    "How old is mouuchii? ":"C",
    "Who gave birf to mouuchii? ":"D"
}

options =[
	["A. Grass", "B. Closet", "C. Leo", "D. Fire"],
	["A. Gardenin", "B. Dunkin on other kittens", "C. Sleepin", "D. Eatin"],
	["A. 1 year old", "B. 69 years old", "C. 4.5 Baboy years old", "D. 18 years old"],
	["A. Omni", "B. Ting Ting", "C. Tissue person", "D. Dammi"]
]

new_game()