package com.poscodxT.demo.service;

import com.poscodxT.demo.domain.Member;
import com.poscodxT.demo.repository.MemoryMemberRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class MemberServiceTest {
    MemberService memberService = new MemberService(); // member service
    MemberService memberService;
    MemoryMemberRepository memberRepository;
    @Test
    void 회원가입() {
        // given
        Member member = new Member(); // member 객체 생성
        member.setName("hello"); // member name에 hello을 넣음

        // when
        // member 객체를 회원가입하고, 반환된 id를 saveId
        Long saveId = memberService.join(member);

        // then
        // 회원가입한 member의 id가 저장소에 있으면, 해당 member 객체를 findMember로
        Member findMember = memberService.findOne(saveId).get();
        // 회원가입한 member와, 저장소에서 가져온 member의 이름이 같은 지 검증
        Assertions.assertThat(member.getName()).isEqualTo(findMember.getName());
    }
    @Test
    public void 중복_회원_예외() {
        // given
        // 이름이 같은 중복 회원 member 객체 생성
        Member member1 = new Member();
        member1.setName("spring");

        Member member2 = new Member();
        member2.setName("spring");

        // when
        memberService.join(member1);

        // memberService.join(member2)에 IllegalStateException 예외 검증
        IllegalStateException e = assertThrows(IllegalStateException.class,
                () -> memberService.join(member2));
        System.out.println(e.getMessage()); // 예외 메시지 출력
    }

    MemoryMemberRepository memberRepository = new MemoryMemberRepository();

    @AfterEach // 메서드 실행이 끝날 때마다 실행됨
    public void afterEach() {
        memberRepository.clearStore(); // 저장소 내용 다 지움
    }
}