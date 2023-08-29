package com.poscodx.study.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller // spring framework 를 사용하기 위해 지정한다.
public class HelloController {
    @GetMapping("hello") //웹 어플리케이션에서 /hello로 들어오면 해당 메서드 호춣
    public String hello(Model model) {
        model.addAttribute("data", "hello!!");
        // attribute 의 이름이 "data"인 곳에 value 로 "hello!!" 가 들어감
        return "hello";
    }

    @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam("name") String name, Model model) {
        // 외부에서 param 을 받음
        model.addAttribute("name", name);
        return "hello-template";
    }

    @GetMapping("hello-string")
    @ResponseBody
    public String helloString(@RequestParam("name") String name) {
        return "hello " + name;
    }

//    http://localhost:8080/hello-string?name=spring!!!

    @GetMapping("hello-api")
    @ResponseBody // http의 body에 param으로 받은 data를 직접 넣어줌
    public Hello helloApi(@RequestParam("name") String name) {
        Hello hello = new Hello();
        hello.setName(name);
        return hello; // hello 객체를 return
    }

    static class Hello {
        private String name; // private 라서 메서드를 사용해 활용

        public String getName() { // getter
            return name;
            //spring
        }

        public void setName(String name) { // setter
            this.name = name;
        }
    }

}
