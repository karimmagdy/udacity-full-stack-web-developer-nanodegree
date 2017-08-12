from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, MenuItem, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


###############################
#Soccer
#Basketball
#Baseball
#Frisbee
#Snowboarding
#Rock Climbing
#Foosball
#Skating
#Hockey
##############################
#Stick                 (Hocky)
#Goggles        (Snowboarding)
#Snowboard      (Snowboarding)
#Two shinguards       (Soccer)
#Shingguards          (Soccer)
#Frisbee             (Frisbee)
#Bat                (Baseball)
#Jesey                (Soccer)
#Soccer Cleats        (Soccer)
##############################


# Create dummy user
User1 = User(name="Karim Magdy", email="karim@gmail.com",
             picture='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_zcvnKkf1GZB_Wz31-uAVhvucZL4M0uKxLTHlrbFpNPFgsgJ1eBIzVA')
session.add(User1)
session.commit()
#########################################################################################################################
# Menu for Soccer
Category1 = Category(user_id=1, name="Soccer")

session.add(Category1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Two shinguards", description="Two shinguards Description.",
                      category=Category1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Shingguards", description="Shingguards Description.",
                      category=Category1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Jesey", description="Jesey Description.",
                      category=Category1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Soccer Cleats", description="Soccer Cleats Description.",
                      category=Category1)

session.add(menuItem3)
session.commit()

#######################################################################################################################
# Menu for Basketball
Category2 = Category(user_id=1, name="Basketball")

session.add(Category2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Basketball item 1", description="Basketball Item 1 Description.",
                      category=Category2)

session.add(menuItem1)
session.commit()

#######################################################################################################################
# Menu for Baseball
Category2 = Category(user_id=1, name="Baseball")

session.add(Category2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Bat", description="Bat Description.",
                      category=Category2)

session.add(menuItem1)
session.commit()

#######################################################################################################################
# Menu for Frisbee
Category1 = Category(user_id=1, name="Frisbee")

session.add(Category1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Frisbee", description="Frisbee Description.",
                     category=Category1)

session.add(menuItem1)
session.commit()

##################################################################################################
# Menu for Snowboarding
Category1 = Category(user_id=1, name="Snowboarding")

session.add(Category1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Goggles", description="Goggles Description.",
                     category=Category1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Snowboard", description="Snowboard Description.",
                     category=Category1)

session.add(menuItem2)
session.commit()

############################################################################################################
# Menu for Rock Climbing
Category1 = Category(user_id=1, name="Rock Climbing")

session.add(Category1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Rock Climbing Item 1", description="Rock Climbing Item 1 Description.",
                     category=Category1)

session.add(menuItem1)
session.commit()

#################################################################################################################
# Menu for Foosball
Category1 = Category(user_id=1, name="Foosball")

session.add(Category1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Foosball Item 1", description="Foosball Item 1 Description.",
                     category=Category1)

session.add(menuItem1)
session.commit()

########################################################################################################
# Menu for Skating
Category1 = Category(user_id=1, name="Skating")

session.add(Category1)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Skating Item 1",
                     description="Skating Item 1 Description.", category=Category1)

session.add(menuItem9)
session.commit()

#################################################################################################################
# Menu for Hockey
Category1 = Category(user_id=1, name="Hockey")

session.add(Category1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Stick",
                     description="Stick Description", category=Category1)

session.add(menuItem1)
session.commit()
#################################################################################################################
print "added menu items!"
