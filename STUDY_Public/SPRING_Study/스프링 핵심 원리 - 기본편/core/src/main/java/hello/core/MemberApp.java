package hello.core;

import hello.core.member.Grade;
import hello.core.member.Member;
import hello.core.member.MemberSerivce;
import hello.core.member.MemberSerivceImpl;

public class MemberApp {
    public static void main(String[] args){
        MemberSerivce memberSerivce = new MemberSerivceImpl();
        Member member =new Member(1L,"memberA", Grade.VIP);
        memberSerivce.join(member);

        Member findMember= memberSerivce.findMember(1L);
        System.out.println("new member" + member.getName());
        System.out.println("new member" + findMember.getName());
    }
}
