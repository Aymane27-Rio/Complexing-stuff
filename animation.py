from manim import *

class AnimatedFormula(Scene):
    def construct(self):

        

        formula_intro = Tex(r"We have the following formula that I found online")
        formula_explanation = Tex(r"\[5\int_{0}^{\infty} \frac{x^2}{(1+x^5)} \,dx = \frac{\pi}{\varphi}. \quad (1)\]")
        VGroup(formula_intro, formula_explanation).arrange(DOWN)
        self.play(
            Write(formula_intro),
            FadeIn(formula_explanation, shift=DOWN),
            )
        self.wait(2)

        text = Tex(r"Hmm, yes, very beautiful.")
        self.play(Transform(formula_intro, text),
                  LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in formula_explanation]),
                  )
        self.wait()

        text1 = Tex("But let's just make things a little bit more complicated because we - human beings - love dramas :3").scale(0.8)
        self.play(
            Transform(formula_intro, text1)
           )
        self.wait(2)

        text2 = Tex("First of all, let's take a look at that 1 in the denominator. We know that for any given \(x \in \mathbb{R}\) we have the following formula :").scale(0.8)
        text3 = Tex(r"\[\cos^2(x) + \sin^2(x) = 1\]")
        VGroup(text2, text3).arrange(DOWN)
        self.play(
            Transform(formula_intro, text2),
            FadeIn(text3, shift=DOWN),
        )
        self.wait(3)

        text4 = Tex("But we want to make things more complicated right?").scale(0.8)
        self.play(
            Transform(formula_intro, text4),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in text3])
        )
        self.wait(1)

        text5 = Tex("Okay then let's head to Taylor and see what he got for us. His formula goes as the following/ For any real or complex-valued function \(f\) that is infinitely differentiable at any real or complex \(a\), we have the following series :").scale(0.7)
        text6 = Tex(r"\[\sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n = f(x)\]")
        text7 = Tex(r"Where \(f^{(n)}(a)\) represents the \(n\)-th derivative of \(f\) evaluated at \(a\).").scale(0.8)

        VGroup(text5, text6, text7).arrange(DOWN)
        self.play(
            Transform(formula_intro, text5),
            FadeIn(text6, shift=DOWN),
            FadeIn(text7, shift=DOWN),
        )
        self.wait(4)

        text8 = Tex("And we know for instance that both the functions \(cos\) and \(sin\) are infinitely differentiable at any given value of \(a\), thus by choosing \(0\), we get the two following formulas :").scale(0.7)
        text9 = Tex(r"\[\cos(x) = \sum_{n=0}^{\infty} \frac{x^{2n}}{(2n)!}, \quad\sin(x) = \sum_{n=0}^{\infty} \frac{x^{2n+1}}{(2n+1)!}\]")
        VGroup(text8, text9).arrange(DOWN)
        self.play(
            Transform(formula_intro, text8),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in text6]),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in text7]),
            FadeIn(text9, shift=DOWN),
        )
        self.wait(6)

        text10 = Tex("Now we have at the least a substitute for that teeny tiny 1 in the denominator").scale(0.8)
        self.play(
            Transform(formula_intro, text10),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in text9]),
        )
        self.wait(2)

        text11 = Tex("For the other sideof the formula, let's take a look at that \(\pi\). A really fascinating number. Take any circle you can think of, then take its circumference and divide it by its diameter. You'll always find the exquisite number \(\pi\).").scale(0.7)
        self.play(
            Transform(formula_intro, text11)
        )
        self.wait(6)       

        text12 = Tex("And who of the many brilliant mathematicians have confronted that number too?").scale(0.8)
        self.play(
            Transform(formula_intro, text12))
        self.wait(1)
        

        text01 = Tex("That's right!")
        self.play(
            Transform(formula_intro, text01)
        )
        self.wait()

        text02 = Tex("The famous Ramanujan Srinivasa who came up with the one of the most counterintuitive results one can ever think of which is:").scale(0.8)
        text13 = Tex(r"\[\sum_{n=1}^{\infty} n = -\frac{1}{12}\]")
        VGroup(text02, text13).arrange(DOWN)
        self.play(
            Transform(formula_intro, text02),
            FadeIn(text13, shift=DOWN),
        )
        self.wait(4)

        text14 = Tex("For now, let's see how did Ramanujan interact with \(\pi\) :").scale(0.8)
        text15 = Tex(r"\[\frac{1}{\pi} = \frac{2\sqrt{2}}{9801} \sum_{n=0}^{\infty} \frac{(4n)!(1103+26390n)}{(n!)^4 396^{4n}}\]")
        VGroup(text14, text15).arrange(DOWN)
        self.play(
            Transform(formula_intro, text14),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in text13]),
            FadeIn(text15, shift=DOWN),
        )
        self.wait(4)

        text16 = Tex("Regarding his discovery of this formula, Ramanujan didn't leave behind any detailed record of his thought process or derivations.").scale(0.8)
        self.play(
            Transform(formula_intro, text16),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in text15])
        )
        self.wait(3)

        text17 = Tex("Nevertheless, we will trust his profound insight and use it to complex the given formula at first").scale(0.8)
        self.play(
            Transform(formula_intro, text17)
        )
        self.wait(3)

        text18 = Tex("By combining the results we have found, let's welcome this dramatic new expression:").scale(0.8)
        text19 = Tex(r"\[5\int_{0}^{\infty} \frac{x^2}{\left(\left(\sum_{n=0}^{\infty} \frac{z^{2n}}{(2n)!}\right)^2 + \left(\sum_{n=0}^{\infty} \frac{z^{2n+1}}{(2n+1)!}\right)^2 + x^5\right)} \,dx = \frac{9801}{\varphi 2\sqrt{2}} \left(\sum_{n=0}^{\infty} \frac{(4n)!(1103+26390n)}{(n!)^4 396^{4n}}\right)^{-1}\]").scale(0.6)
        VGroup(text18, text19).arrange(DOWN)
        self.play(
            Transform(formula_intro, text18),
            FadeIn(text19, shift=DOWN),
        )
        self.wait(5)

        text20 = Tex("and voilà! :D")
        self.play(
            Transform(formula_intro, text20),
            LaggedStart(*[FadeOut(obj, shfit=DOWN) for obj in text19])
        )
        self.wait(1)
        self.play(FadeOut(formula_intro))
