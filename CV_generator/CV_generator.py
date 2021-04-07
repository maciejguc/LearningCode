import json

with open("data.json") as file:
    data = json.load(file)


def cv_gen():
    for person in data:
        head = f"""<html lang="en">
        <head>
            <meta charset="UTF-8" />
            <title>CV generator</title>
            <link rel="stylesheet" type="text/css" href="style_cv.css" />
        </head> """

        sidebar = f"""<body>
            <div id="sidebar">
                    <div class="profile">
                    <img src="{data[person]["picture"]}" alt="Couldn't locate image">
                    </div>"""

        contact = f"""
            <div class="contact blue">
                <h3>CONTACT</h3>
                    <ul>
                        <li id="ln"><a href="#">{data[person]["name"]}</a><li>
                        <li id="phone">{data[person]["phone"]}</li>
                        <li id="mail">{data[person]["email"]}</li>
                        <li id="address">{data[person]["address"]}</li>
                    </ul>
                </div>
            </div> """

        main_info = f"""<div id="main-info">
                <header class="intro">
                    <h1>{data[person]["name"]}</h1>
                        <div class="paragraph">
                            <ul>
                                <li>Age: {data[person]["age"]} </li>
                                <li>Gender: {data[person]["gender"]}</li>
                                <li>Company: {data[person]["company"]}</li>
                                <li><p>{data[person]["about"]}</p></li>
                            </ul>
                        </div>
                </header> """

        skills = f"""
                    <div class="division blue">
                    <h3>SKILLS</h3>
                        <div class="paragraph">
                            <p class="list-title">Skills:</p> <ul> """

        def list_skills():
            skill_list = ""
            for element in data[person]["skills"]:
                skill_list += f"<li>{element['skill']} - {element['grade']}</li>"
            return skill_list

        skills += list_skills()

        skills += f""" </ul>
                        </div>
                    </div> """

        education = f"""
                    <div class="division blue">
                    <h3>EDUCATION</h3>
                        <div class="paragraph"><p>"""

        def education_list():
            school_list = ""
            for element in data[person]["education"]:
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

        file_name = person.replace(" ", "_")
        html = head + sidebar + contact + main_info + skills + education
        f = open(f"{file_name}.html", "w")
        f.write(html)
        f.close()


cv_gen()

landing = f"""<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="stylesheet" type="text/css" href="style_landing.css" />
        <title>Document</title>
    </head>
    <body>
        <div class="main">
        <h3>CV list</h3>
        <ul>"""


def cv_list():
    people_list = ""
    for person in data:
        file_name = person.replace(" ", "_")
        people_list += (
            f"""<li><a href="../CV_generator/{file_name}.html">{person}</a></li>"""
        )
    return people_list


landing += cv_list()
landing += f"""
            </ul>
            </div>
        </body>
        </html>"""

f = open(f"index.html", "w")
f.write(landing)
f.close()
