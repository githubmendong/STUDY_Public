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

    private final MemberRepository memberRepository = new MemoryMemerRepository(); //final : 변경할 수 없는 상수값

    /*
    회원 가입
     */
    public Long join(Member member) {
        //같은 이름인 중복 회원 X
        validateDuplicateMember(member);

        memberRepository.save(member);
        return member.getId();
    }

    private void validateDuplicateMember(Member member) {

        memberRepository.findByName(member.getName()) //일단 이름을 찾아본다
                .ifPresent(m -> {  //이미 그 이름이 존재한다면,  ifPresent() : null이 아니라 값이 있으면 다음 동작이 실행된다.
                    throw new IllegalStateException("이미 존재하는 회원입니다.");
                });

//        Optional<Member> result = memberRepository.findByName(member.getName());
//        result.ifPresent(m -> {
//            throw new IllegalStateException("이미 존재하는 회원입니다.");
//        });
    }

    /*
    전체 회원 조회
     */
    public List<Member> findMembers() {
        return memberRepository.findAll(); //findAll의 반환 타임 : List
    }

    public Optional<Member> findOne(Long memberId) {
        return memberRepository.findById(memberId);
    }
}
