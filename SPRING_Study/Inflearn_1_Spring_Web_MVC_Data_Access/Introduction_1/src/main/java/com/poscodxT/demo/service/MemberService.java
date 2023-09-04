package com.poscodxT.demo.service;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.ui.Model;

@Controller // spring framework 를 사용하기 위해
public class HelloController {

    private final MemberRepository memberRepository = new MemoryMemberRepository();


    // 회원가입

    public Long join(Member member){
        memberRepository.findByName(member.getName())


                return member.getId();

    }
}
