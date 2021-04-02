import json

with open("data.json") as file:
    data = json.load(file)

color_choice = input("Provide color choice (RED/BLUE): ")
if color_choice.upper() == "RED":
    color_class = "red"

elif color_choice.upper() == "BLUE":
    color_class = "blue"

else:
    print("Instructions unclear. Setting color to default.")
    color_class = "blue"

f = open("CV.html", "w")

head = f"""<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>CV generator</title>
    <link rel="stylesheet" type="text/css" href="style.css" />
  </head> """

sidebar = f"""<body>
    <div id="sidebar">
            <div class="profile">
            <img src="{data["picture"]}" alt="Couldn't locate image">
            </div>"""

contact = f"""
    <div class="contact {color_class}">
        <h3>CONTACT</h3>
            <ul>
                <li id="ln"><a href="#">{data["name"]}</a><li>
                <li id="phone">{data["phone"]}</li>
                <li id="mail">{data["email"]}</li>
                <li id="address">{data["address"]}</li>
            </ul>
        </div>
    </div> """

main_info = f"""<div id="main-info">
        <header class="intro">
            <h1>{data["name"]}</h1>
                <div class="paragraph">
                    <ul>
                        <li>Age: {data["age"]} </li>
                        <li>Gender: {data["gender"]}</li>
                        <li>Company: {data["company"]}</li>
                        <li><p>{data["about"]}</p></li>
                    </ul>
                </div>
        </header> """

# education = (f"""<experience>
#             <div class="division">
#             <h3>SKILLS</h3>
#                 <div class="paragraph"> """)
#                    <p>Some text</p>
#               </div>
#             </div>
#         </experience> """)

skills = f"""
            <div class="division {color_class}">
            <h3>SKILLS</h3>
                <div class="paragraph">
                    <p class="list-title">Skills:</p> <ul> """


def list_skills():
    skill_list = ""

    for element in data["skills"]:
        grade = ""
        for i in range((int(element["grade"]))):
            grade += "*"
        skill_list += f"<li>{element['skill']} - {grade}</li>"
    return skill_list


skills += list_skills()

skills += f""" </ul>
                </div>
            </div> """

education = f"""
            <div class="division {color_class}">
            <h3>EDUCATION</h3>
                <div class="paragraph"><p>"""


def education_list():
    school_list = ""
    for element in data["education"]:
        school_list += f"<br><br>{element['name']}<br>{element['time']}"
    return school_list


education += education_list()

education += f"""</p>
              </div>
            </div>
      </div>
    </div>
  </body>
</html> """

html = head + sidebar + contact + main_info + skills + education
f.write(html)
f.close()