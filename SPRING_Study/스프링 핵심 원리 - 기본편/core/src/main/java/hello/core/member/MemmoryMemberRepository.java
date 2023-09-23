package hello.core.member;

public interface MemmoryMemberRepository {

    void save(Member member);
    Member findById(Long memberId);
}
