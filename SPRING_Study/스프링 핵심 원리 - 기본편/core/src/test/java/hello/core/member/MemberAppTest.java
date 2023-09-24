//package hello.core.member;
//
//import hello.core.member.Grade;
//import hello.core.member.Member;
//import hello.core.member.MemberSerivce;
//import hello.core.member.MemberSerivceImpl;
//import org.junit.jupiter.api.Assertions;
//import org.junit.jupiter.api.Test;
//
//import static org.junit.jupiter.api.Assertions.*;
//
//class MemberAppTest {
//    MemberService memberService = new MemberServiceImpl();
//
//    @Test
//    void main() {
//
//
//        //given
//        Member member = new Member(1L, "memberA", Grade.VIP);
//        //when
//        memberService.join(member);
//        Member findMember = memberService.findMember(1L);
//        //then
//        Assertions.assertThat(member).isEqualTo(findMember);
//
//
//    }
//}