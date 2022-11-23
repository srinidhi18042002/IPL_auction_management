from tkinter import *
import mysql.connector
from PIL import ImageTk, Image

window = Tk()
valid=0
window.title("IPL 2023")
window.geometry('400x400')
canv = Canvas(window, width=400, height=224, bg='white')
canv.grid(row=2, column=3)

img = ImageTk.PhotoImage(Image.open("ipl.png"))  # PIL solution
canv.create_image(20, 20, anchor=NW, image=img)


lbl = Label(window, text="Hello Admin, Welcome to IPL Auctioning", font=("Arial Bold", 20))
lbl.grid(column=0,row=0)
def clicked():
	#window1=Tk()
	window.title("Admin Login_IPL2023")
	login_label=Label(window, text="Admin Credentials:")
	login_label.grid(column=20,row=10)
	login_id_label=Label(window,text="ID: ")
	login_id_label.grid(column=20,row=11)
	id_txt=Entry(window,width=10)
	id_txt.grid(column=25,row=11)
	login_pw_label=Label(window,text="PW: ")
	login_pw_label.grid(column=20,row=15)
	pw_txt=Entry(window,width=10)
	pw_txt.grid(column=25,row=15)	
	def clicked_1():
		if id_txt.get() == "hey" and pw_txt.get() == "sup":
			window.title("Welcome")
			after_login_label=Label(window,text="you have logged in successfully")
			after_login_label.grid(column=50,row=50)
			main_window=Tk()
			main_window.title("Welcome.Happy auctioning")
			main_window.geometry('350x200')
			def insert():
				insert_window=Tk()
				insert_window.title("insertion")
				

				player_id_label=Label(insert_window,text="Player_ID")
				player_id_label.grid(column=1,row=5)
				player_id_txt=Entry(insert_window,width=10)
				player_id_txt.grid(column=2,row=5)
				
				player_teamname_label=Label(insert_window,text="Team_name")
				player_teamname_label.grid(column=1,row=10)
				player_teamname_txt=Entry(insert_window,width=10)
				player_teamname_txt.grid(column=2,row=10)

				player_baseprice_label=Label(insert_window,text="Base_Price")
				player_baseprice_label.grid(column=1,row=15)
				player_baseprice_txt=Entry(insert_window,width=10)
				player_baseprice_txt.grid(column=2,row=15)

				player_name_label=Label(insert_window,text="Player_name")
				player_name_label.grid(column=1,row=20)
				player_name_txt=Entry(insert_window,width=10)
				player_name_txt.grid(column=2,row=20)

				player_type_label=Label(insert_window,text="Player_type")
				player_type_label.grid(column=1,row=25)
				player_type_txt=Entry(insert_window,width=10)
				player_type_txt.grid(column=2,row=25)
				'''chk_state_1 = BooleanVar()
				chk_state_1.set(True) #set check state
				chk_1 = Checkbutton(insert_window, text='Batsmsn', var=chk_state_1)
				chk_1.grid(column=2, row=30)

				chk_state_2 = BooleanVar()
				chk_state_2.set(True) #set check state
				chk_2 = Checkbutton(insert_window, text='Allrounder', var=chk_state_2)
				chk_2.grid(column=2, row=35)
				
				chk_state_3 = BooleanVar()
				chk_state_3.set(True) #set check state
				chk_3 = Checkbutton(insert_window, text='BOWLER', var=chk_state_3)
				chk_3.grid(column=2, row=40)

				chk_state_4 = BooleanVar()
				chk_state_4.set(True) #set check state
				chk_4 = Checkbutton(insert_window, text='WK', var=chk_state_4)
				chk_4.grid(column=2, row=25)'''

				player_country_label=Label(insert_window,text="Player_country")
				player_country_label.grid(column=1,row=45)
				player_country_txt=Entry(insert_window,width=10)
				player_country_txt.grid(column=2,row=45)

				player_wickets_label=Label(insert_window,text="Wickets_taken")
				player_wickets_label.grid(column=1,row=50)
				player_wickets_txt=Entry(insert_window,width=10)
				player_wickets_txt.grid(column=2,row=50)


				player_runs_label=Label(insert_window,text="Runs_scored")
				player_runs_label.grid(column=1,row=55)
				player_runs_txt=Entry(insert_window,width=10)
				player_runs_txt.grid(column=2,row=55)

				player_aucid_label=Label(insert_window,text="Auction_ID")
				player_aucid_label.grid(column=1,row=60)
				player_aucid_txt=Entry(insert_window,width=10)
				player_aucid_txt.grid(column=2,row=60)



				player_bought_for_label=Label(insert_window,text="Player sold for")
				player_bought_for_label.grid(column=1,row=65)
				player_bought_for_txt=Entry(insert_window,width=10)
				player_bought_for_txt.grid(column=2,row=65)


				def topG():

					mydb=mysql.connector.connect(
						host="localhost",
						user="root",
						password="1234",
						database="ipl_auction")
					mycursor=mydb.cursor()
					
					sql="insert into player (player_id,player_team_name,base_price,player_name,player_type,wickets_take,runs_scored,player_country,year_of_auction,player_auc_id,player_sold_for) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
					val=(player_id_txt.get(),player_teamname_txt.get(),player_baseprice_txt.get(),player_name_txt.get(),player_type_txt.get(),player_wickets_txt.get(),player_runs_txt.get(),player_country_txt.get(),"2023",player_aucid_txt.get(),player_bought_for_txt.get())
					mycursor.execute(sql,val)
					mydb.commit()
					mydb.close()
					clicked_1()
			
				submit_btn=Button(insert_window,text="submit",command=topG)
				submit_btn.grid(column=50,row=50)
			
			insert_btn= Button(main_window,text="insert record",command=insert)
			insert_btn.grid(column=1,row=1)


			sql_cmd_label=Label(main_window,text="SQL query:")
			sql_cmd_label.grid(column=119,row=110)
			sql_text=Entry(main_window,width=100)
			sql_text.grid(column=120,row=110)

			def sqlex():
				mydb=mysql.connector.connect(
						host="localhost",
						user="root",
						password="1234",
						database="ipl_auction")
				mycursor2=mydb.cursor()
				sql=sql_text.get()
				mycursor2.execute(sql)
				y=mycursor2.fetchall()
				output_sql=Label(main_window,text=y)
				output_sql.grid(column=120,row=120)



			sql_btn=Button(main_window,text="execute query",command=sqlex)
			sql_btn.grid(column=120,row=111)
			# def retrieve():
			# 	ret_window=Tk()
			# 	ret_window.title("retrieve")
			# retrieve_btn= Button(main_window,text=" retrieve record",command=retrieve)
			# retrieve_btn.grid(column=20,row=25)
			def modify():
				update_window=Tk()
				update_window.title("modify")
				team_name=Label(update_window,text="Team name: ")
				team_name.grid(column=1,row=1)
				team_name_txt=Entry(update_window,width=20)
				team_name_txt.grid(column=2,row=1)
				temp=team_name_txt.get()
				updated_budget=Label(update_window,text="uPDATED BUDGET spent: ")
				updated_budget.grid(column=1,row=2)
				updated_budget_txt=Entry(update_window,width=20)
				updated_budget_txt.grid(column=2,row=2)
				temp2=updated_budget_txt.get()
				updated_budget_two=Label(update_window,text="uPDATED BUDGET left: ")
				updated_budget_two.grid(column=1,row=3)
				updated_budget_two_txt=Entry(update_window,width=20)
				updated_budget_two_txt.grid(column=2,row=3)
				temp3=updated_budget_two_txt.get()
				
				
				def upd1():
						mydb2=mysql.connector.connect(
							host="localhost",
							user="root",
							password="1234",
							database="ipl_auction")
						mycursor2=mydb2.cursor()
						sql2="update team set purse_spent_in_rupees = (%s) where team_name= (%s)"
						val2=(updated_budget_txt.get(),team_name_txt.get())
						#sql3="update team set purse_remaining_in_rupees = (%s) where team_name= (%s)"
						#val3=(updated_budget_two_txt.get())
						#mycursor2.execute(sql3,val3)
						mycursor2.execute(sql2,val2)
						mydb2.commit()
						mydb2.close()

				def upd2():
						mydb4=mysql.connector.connect(
							host="localhost",
							user="root",
							password="1234",
							database="ipl_auction")
						mycursor4=mydb4.cursor()
						#sql2="update team set purse_spent_in_rupees = (%s) where team_name= (%s)"
						#val2=(updated_budget_txt.get(),team_name_txt.get())
						sql7="update team set purse_remaining_in_rupees = (%s) where team_name= (%s)"
						val7=(updated_budget_two_txt.get(),team_name_txt.get())
						mycursor4.execute(sql7,val7)
						#mycursor2.execute(sql2,val2)
						mydb4.commit()
						mydb4.close()
						clicked_1()

	
				update_record_btn= Button(update_window,text="Update record",command=upd1)
				update_record_btn.grid(column=3,row=2)
				update_record_two_btn= Button(update_window,text="Update record",command=upd2)
				update_record_two_btn.grid(column=3,row=3)
				
				


			update_btn= Button(main_window,text="modify record",command=modify)
			update_btn.grid(column=2,row=1)
			def delete():
				del_window=Tk()
				del_window.title("deletion")
				Player_tbd= Label(del_window,text="Player id: ")
				Player_tbd.grid(column=1,row=1)
				Player_tbd_txt= Entry(del_window,width=10)
				Player_tbd_txt.grid(column=2,row=1)
				

				def delsql():
					mydb6=mysql.connector.connect(
							host="localhost",
							user="root",
							password="1234",
							database="ipl_auction")
					mycursor6=mydb6.cursor()
					# sql4="delete from previous_records where prevrec_player_id = (%s)"
					# #sql5="delete from player where player_id = %s"
					# val5=(Player_tbd_txt.get())
					mycursor6.execute("delete from previous_records where prevrec_player_id = (%s)" % (Player_tbd_txt.get()) )
					mycursor6.execute("delete from award where award_player_id = (%s)" % (Player_tbd_txt.get()))
					mycursor6.execute("delete from player where player_id = (%s)" % (Player_tbd_txt.get()))
					mydb6.commit()
					mydb6.close()
					clicked_1()
				del_btn=Button(del_window,text="Delete",command=delsql)
				del_btn.grid(column=1,row=2)


			del_btn= Button(main_window,text="delete record",command=delete)
			del_btn.grid(column=3,row=1)
			def budget():
				mydb=mysql.connector.connect(
						host="localhost",
						user="root",
						password="1234",
						database="ipl_auction")
				mycursor1=mydb.cursor()
				q1="select distinct player_team_name,get_budget(%s) from player where player_team_name = (%s)"
				v1=(budget_avg_txt.get(),budget_avg_txt.get())
				mycursor1.execute(q1,v1)
				x=mycursor1.fetchall()
				budget_remaining=Label(main_window,text=x)
				budget_remaining.grid(column=100,row=100)


			budget_avg=Label(main_window,text="Budget and avg of team: ")
			budget_avg.grid(column = 1, row=3)
			budget_avg_txt=Entry(main_window,width=10)
			budget_avg_txt.grid(column = 2, row = 3)
			budget_btn=Button(main_window,text="get budget and avg",command=budget)
			budget_btn.grid(column=1,row=4)	
		else:
			error_login_label=Label(window,text="incorrect details")
			valid=0
			error_login_label.grid(column=25,row=30)
			
	btn1= Button(window,text="log in",command=clicked_1)	
	btn1.grid(column=25,row=25)
	
btn= Button(window, text="Admin Login", bg="yellow",fg="purple",command=clicked)

btn.grid(column=10,row=10)

'''

	main_window=Tk()
	main_window.title("Welcome.Happy auctioning")
	main_window.geometry('350x200')
	insert_btn= Button(main_window,text="insert record",command=insert)
	insert_btn= Button(main_window,text=" retrieve record",command=retrieve)
	insert_btn= Button(main_window,text="update record",command=update)
	insert_btn= Button(main_window,text="delete record",command=del)
	
	
'''
	

window.mainloop()



#print("hello")
