package com.poscodxT.demo.service;

import com.poscodxT.demo.domain.Member;
import com.poscodxT.demo.repository.MemoryMemberRepository;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.ui.Model;

import java.util.List;
import java.util.Optional;

@Controller // spring framework 를 사용하기 위해
public class MemberService {

    // 저장소
    private final MemberRepository memberRepository = new MemoryMemberRepository();

    // 회원가입
    public Long join(Member member) {

        // 중복회원 검증 메서드 호출
        validateDuplicateMember(member);

        // member를 저장소에 저장
        memberRepository.save(member);
        // member id 반환
        return member.getId();
    }

    // 중복회원 검증 메서드
    private void validateDuplicateMember(Member member) {
        memberRepository.findByName(member.getName()).ifPresent(m -> { // 이름이 같은 회원이 존재하면
            throw new IllegalStateException("이미 존재하는 회원입니다.");
        });
    }

    //전체 회원 조회 메서드
    public List<Member> findMembers(){
        return memberRepository.findAll();
    }

    //id 회원 조회 서비스
    public Optional<Member> findOne(Long memberId){
        return memberRepository.findById(memberId);
    }
}
