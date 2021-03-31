import json
with open('data.json') as file:
  data = json.load(file)

color_choice = input("Provide color choice (RED/BLUE): ")
if color_choice.upper() == "RED":
    line_color = "rgb(220, 20, 60)"

elif color_choice.upper() == "BLUE":
    line_color = "rgb(62, 168, 255)"

else:
    print("Instructions unclear. Setting line color to default.")
    line_color = "rgb(62, 168, 255)"

f = open('style.css', 'a')
css = f"""
    border-top:"""+line_color+"""3px solid;}

.division {
    padding-top: 10px;
    border-top: """+line_color+"""3px solid;}"""

f.write(css)
f.close

f = open('CV.html', 'w')

head = (f"""<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>CV generator</title>
    <link rel="stylesheet" type="text/css" href="style.css" />
  </head> """)


sidebar = (f"""<body>
    <div id="sidebar">
        <image>
            <div class="profile">
            <img src="{data["picture"]}" alt="Couldn't locate image">
            </div>
        </image> """)

contact = (f"""<contact>
            <div class="contact red">
                <h3>CONTACT</h3>
                <ul>
                    <li id="ln"><a href="#">{data["name"]}</a><li>
                    <li id="phone">{data["phone"]}</li>
                    <li id="mail">{data["email"]}</li>
                    <li id="address">{data["address"]}</li>
                </ul>
            </div>
        </contact>
    </div> """)

main_info = (f"""<div id="main-info">
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
        </header> """)

# education = (f"""<experience>
#             <div class="division">
#             <h3>SKILLS</h3>
#                 <div class="paragraph"> """)
#                    <p>Some text</p>
#               </div>
#             </div>
#         </experience> """)

skills = (f"""<skills>
            <div class="division red">
            <h3>SKILLS</h3>
                <div class="paragraph">
                    <p class="list-title">Skills:</p> <ul> """)

def list_skills():
    skill_list = ""

    for element in data["skills"]:
        grade = ""
        for i in range((int(element['grade']))):
            grade += "*"
        skill_list += (f"<li>{element['skill']} - {grade}</li>")
    return skill_list

skills += list_skills()

skills += (f""" </ul>
                </div>
            </div>
        </skills>""")

education = (f"""<education>
            <div class="division">
            <h3>EDUCATION</h3>
                <div class="paragraph"><p>""")

def education_list():
    school_list = ""
    for element in data["education"]:
        school_list += (f"<br><br>{element['name']}<br>{element['time']}")
    return school_list

education += education_list()

education += (f"""</p>
              </div>
            </div>
        </education>
      </div>
    </div>
  </body>
</html> """)

f.write(head)
f.write(sidebar)
f.write(contact)
f.write(main_info)
f.write(skills)
f.write(education)

f.close()