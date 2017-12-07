from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Items, User

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


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/'
                     '2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Kirana
category1 = Category(user_id=1, name="Kirana")
session.add(category1)
session.commit()


item2 = Items(user_id=1,
              name="Burger Mix",
              description="Juicy grilled veggie"
                          " patty with tomato mayo and lettuce",
              category=category1 )
session.add(item2)
session.commit()
item1 = Items(user_id=1,
              name="French Fries Masala",
              description="with garlic and parmesan",
              category=category1)
session.add(item1)
session.commit()
item2 = Items(user_id=1,
              name="Chicken Burger Masala",
              description="Juicy grilled chicken patty "
                          "with tomato mayo and lettuce",
              category=category1)
session.add(item2)
session.commit()
item3 = Items(user_id=1,
              name="Chocolate Cake",
              description="fresh baked and served with ice cream",
              category=category1)
session.add(item3)
session.commit()
item4 = Items(user_id=1,
              name="Sirloin Burger",
              description="Made with grade A beef",
              category=category1)
session.add(item4)
session.commit()
item5 = Items(user_id=1,
              name="Root Beer",
              description="16oz of refreshing goodness",
              category=category1)
session.add(item5)
session.commit()
item6 = Items(user_id=1,
              name="Iced Tea",
              description="with Lemon",
              category=category1)
session.add(item6)
session.commit()
item7 = Items(user_id=1,
              name="Grilled Cheese Sandwich Masala",
              description="On texas toast with American Cheese",
              category=category1)
session.add(item7)
session.commit()
item8 = Items(user_id=1,
              name="Veggie Burger",
              description="Made with freshest of ingredients "
                          "and home grown spices",
              category=category1)
session.add(item8)
session.commit()


#Super Stir Fry Masala
category2 = Category(user_id=1, name="Super Stir Fry Kirana")
session.add(category2)
session.commit()


item1 = Items(user_id=1,
              name="Chicken Stir Fry",
              description="With your choice of noodles "
                          "vegetables and sauces",
              category=category2)
session.add(item1)
session.commit()
item2 = Items(user_id=1,
              name="Peking Duck",
              description=" A famous duck dish from Beijing[1]"
                          " that has been prepared since "
                          "the imperial era."
                          " The meat is prized for its thin, "
                          "crisp skin, with authentic "
                          "versions of the dish serving mostly the"
                          " skin and little meat, "
                          "sliced in front of the diners by the cook",
              category=category2)
session.add(item2)
session.commit()
item3 = Items(user_id=1,
              name="Spicy Tuna Roll",
              description="Seared rare ahi, avocado, "
                          "edamame, cucumber with wasabi soy sauce ",
              category=category2)
session.add(item3)
session.commit()
item4 = Items(user_id=1,
              name="Nepali Momo ",
              description="Steamed dumplings made "
                          "with vegetables, spices and meat. ",
              category=category2)
session.add(item4)
session.commit()
item5 = Items(user_id=1,
              name="Beef Noodle Soup",
              description="A Chinese noodle soup made of "
                          "stewed or red braised beef, beef broth, "
                          "vegetables and Chinese noodles.",
              category=category2)
session.add(item5)
session.commit()

print "added menu items!"