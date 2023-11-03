package com.poscodxT.demo;

import com.poscodxT.demo.domain.Member;
import com.poscodxT.demo.service.MemberService;

public class MemberServiceImpl extends MemberService {
    private final MemberRepository memberRepository;

    public MemberServiceImpl(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    @Override
    public void join(Member member) {
        memberRepository.save(member);
    }

    @Override
    public Member findMember(Long memberId) {
        return memberRepository.findById(memberId);
    }
}