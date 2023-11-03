package hello.core;

import com.poscodxT.demo.OrderServiceImpl;
import com.poscodxT.demo.RateDiscountPolicy;
import com.poscodxT.demo.service.MemberService;
import hello.core.Order.OrderService;
import hello.core.discount.DiscountPolicy;
import hello.core.member.Member;
import hello.core.member.MemberRepository;
import hello.core.member.MemoryMemberRepository;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AppConfig {
	@Bean
	public MemberService memberService(){
		return new MemberService(memberRepository()) {
			@Override
			public Member findMember(Long memberId) {
				return null;
			}
		};
	}
	@Bean
	public OrderService orderService() {
		return (OrderService) new OrderServiceImpl(memberRepository(), discountPolicy(), discountPolicy());
	}
	@Bean
	public MemberRepository memberRepository() {
		return new MemoryMemberRepository();
	}
	@Bean
	public DiscountPolicy discountPolicy() {
		return (DiscountPolicy) new RateDiscountPolicy();
	}

}
