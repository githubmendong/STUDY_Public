package com.poscodxT.demo.controller;

import ch.qos.logback.core.model.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

public class HelloController {

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
        }

        public void setName(String name) { // setter
            this.name = name;
        }
    }
}
