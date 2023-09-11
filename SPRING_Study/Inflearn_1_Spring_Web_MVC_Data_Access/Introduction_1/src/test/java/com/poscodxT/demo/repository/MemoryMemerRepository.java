package com.poscodxT.demo.repository;

import com.poscodxT.demo.domain.Member;

import java.util.List;
import java.util.Optional;

public class MemoryMemerRepository {
    Member save(Member member) //회원이 저장소에 저장된다.
    {
        return null;
    }

    Optional<Member> findById(Long id) //id로 회원을 찾는다.
    {
        return null;
    }

    Optional<Member> findByName(String name) //name으로 회원을 찾는다.
    {
        return null;
    }

    List<Member> findAll() //저장된 회원 리스트를 모두 반환해준다.
    {
        return null;
    }

    public void clearStore() {
    }
}
