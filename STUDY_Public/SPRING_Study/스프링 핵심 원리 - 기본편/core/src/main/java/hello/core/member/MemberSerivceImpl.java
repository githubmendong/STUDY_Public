package hello.core.member;

public class MemberSerivceImpl implements MemberSerivce {

    private final MemberRepository memberRepository = new MemoryMemberRepository();

    public MemberSerivceImpl(MemberRepository memberRepository) {

    }

    @Override
    public void join(Member member){
        memberRepository.save(member);
    }

    @Override
    public Member findMember(Long memberId){
        return memberRepository.findById(memberId);
    }
}
