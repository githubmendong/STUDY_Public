package com.poscodxT.demo.repository;

import com.poscodxT.demo.domain.Member;

import java.util.List;
import java.util.Optional;

public interface MemberReposiory {
    Member save(Member member);
    Optional<Member> findById(Long id);
    Optional<Member> findByName(String name);
    List<Member> findAll();
}
