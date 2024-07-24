import 'package:flutter/material.dart';
import 'package:login_singup/config/palette.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class LoginSignupScreen extends StatefulWidget {
  @override
  _LoginSignupScreenState createState() => _LoginSignupScreenState();
}

class _LoginSignupScreenState extends State<LoginSignupScreen> {
  bool isSignupScreen = true;
  bool isMale = true;
  bool isRememberMe = false;

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Scaffold(
        backgroundColor: Palette.backgroundColor,
        body: Stack(children: [
          Positioned(
            top: 0,
            right: 0,
            left: 0,
            child: Container(
              height: 900,
              decoration: BoxDecoration(
                  image: DecorationImage(
                      image: AssetImage("images/background.jpg"),
                      fit: BoxFit.fill)),
              child: Container(
                padding: EdgeInsets.only(top: 80, left: 70),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    RichText(
                      text: TextSpan(
                        text: "HOŞGELDİN EMİR ",
                        style: TextStyle(
                            fontWeight: FontWeight.bold,
                            fontSize: 25,
                            letterSpacing: 2,
                            color: Color.fromARGB(255, 0, 0, 0)),
                      ),
                    ),
                    SizedBox(
                      height: 10,
                    )
                  ],
                ),
              ),
            ),
          ),
          Positioned(
              top: 150,
              child: Container(
                height: 380,
                padding: EdgeInsets.all(20),
                width: MediaQuery.of(context).size.width - 40,
                margin: EdgeInsets.symmetric(horizontal: 20),
                decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(15),
                    boxShadow: [
                      BoxShadow(
                          color: Colors.black.withOpacity(0.3),
                          blurRadius: 15,
                          spreadRadius: 5),
                    ]),
                child: Column(
                  children: [
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        GestureDetector(
                          onTap: () {
                            setState(() {
                              isSignupScreen = false;
                            });
                          },
                          child: Column(
                            children: [
                              Text(
                                "GİRİŞ",
                                style: TextStyle(
                                    fontSize: 16,
                                    fontWeight: FontWeight.bold,
                                    color: !isSignupScreen
                                        ? Palette.activeColor
                                        : Palette.textColor1),
                              ),
                              if (!isSignupScreen)
                                Container(
                                  margin: EdgeInsets.only(top: 3),
                                  height: 2,
                                  width: 65,
                                  color: Colors.deepPurple,
                                )
                            ],
                          ),
                        ),
                        GestureDetector(
                          onTap: () {
                            setState(() {
                              isSignupScreen = true;
                            });
                          },
                          child: Column(
                            children: [
                              Text(
                                "KAYIT OL",
                                style: TextStyle(
                                    fontSize: 16,
                                    fontWeight: FontWeight.bold,
                                    color: isSignupScreen
                                        ? Palette.activeColor
                                        : Palette.textColor1),
                              ),
                              if (isSignupScreen)
                                Container(
                                  margin: EdgeInsets.only(top: 3),
                                  height: 2,
                                  width: 75,
                                  color: Colors.deepPurple,
                                ),
                            ],
                          ),
                        )
                      ],
                    ),
                    Container(
                      height: size.height / 4,
                      margin: EdgeInsets.only(top: 20),
                      child: Column(
                        children: [
                          Container(
                            child: TextField(
                              decoration: InputDecoration(
                                  prefixIcon: FaIcon(
                                FontAwesomeIcons.user,
                                size: 18,
                              )),
                            ),
                          ),
                        ],
                      ),
                    )
                  ],
                ),
              ))
        ]));
  }
}
