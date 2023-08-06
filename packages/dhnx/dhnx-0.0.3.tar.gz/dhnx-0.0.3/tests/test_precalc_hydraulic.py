import pytest

from dhnx.optimization.precalc_hydraulic import calc_d_p
from dhnx.optimization.precalc_hydraulic import calc_k_v
from dhnx.optimization.precalc_hydraulic import calc_lambda_laminar
from dhnx.optimization.precalc_hydraulic import calc_lambda_rough
from dhnx.optimization.precalc_hydraulic import calc_lambda_transition
from dhnx.optimization.precalc_hydraulic import calc_lambda_turb1
from dhnx.optimization.precalc_hydraulic import calc_lambda_turb2
from dhnx.optimization.precalc_hydraulic import calc_lambda_turb3
from dhnx.optimization.precalc_hydraulic import calc_mass_flow
from dhnx.optimization.precalc_hydraulic import calc_mass_flow_P
from dhnx.optimization.precalc_hydraulic import calc_pipe_loss
from dhnx.optimization.precalc_hydraulic import calc_power
from dhnx.optimization.precalc_hydraulic import calc_Re
from dhnx.optimization.precalc_hydraulic import calc_v
from dhnx.optimization.precalc_hydraulic import calc_v_mf
from dhnx.optimization.precalc_hydraulic import delta_p
from dhnx.optimization.precalc_hydraulic import v_max_bisection
from dhnx.optimization.precalc_hydraulic import v_max_secant


def test_calc_v():
    v = calc_v(720, 0.5)
    assert round(v, 5) == 1.01859


def test_calc_power():
    P_th = calc_power(80, 50, 3)
    assert round(P_th, 5) == 393070.3261


def test_calc_mass_flow():
    mf = calc_mass_flow(3, 0.5, 20)
    assert round(mf, 5) == 587.99192


def test_calc_mass_flow_P():
    mf = calc_mass_flow_P(50000, 20, 5)
    assert round(mf, 5) == 2.3896


def test_calc_v_mf():
    v = calc_v_mf(200, 0.5, 20)
    assert round(v, 5) == 1.02042


def test_calc_pipe_loss():
    loss = calc_pipe_loss(20, 0.1, 10)
    assert round(loss, 5) == 1


def test_calc_k_v():
    k_v = calc_k_v(5, 4)
    assert k_v == 1.25


def test_calc_Re():
    Re = calc_Re(1, 2, 4)
    assert Re == 0.5


def test_calc_lam_laminar():
    lam = calc_lambda_laminar(64)
    assert lam == 1


def test_calc_d_p():
    dp = calc_d_p(1, 1, 2, 1, 2)
    assert dp == 1


def test_calc_lam_turb1():
    lam = calc_lambda_turb1(0.001)
    assert round(lam, 5) == 1.77925


def test_calc_lam_turb2():
    lam = calc_lambda_turb2(1)
    assert lam == 0.2242


def test_calc_lam_rough():
    lam = calc_lambda_rough(1, 1)
    assert round(lam, 5) == 0.77116


def test_calc_lam_turb3():
    lam = calc_lambda_turb3(1)
    assert round(lam, 5) == 12.18494


def test_calc_lam_transition():
    lam = calc_lambda_transition(1, 1, 1)
    assert round(lam, 5) == 23.41445


def test_wrong_initial_guess_error():
    with pytest.raises(AttributeError, match=r"initial guesses `v_0` and "):
        v_max_bisection(0.1, 65, v_0=1, v_1=1)


def test_bisection_method_velocity():
    bi_1 = v_max_bisection(
        0.1, 65, k=0.1, p_max=100,
        p_epsilon=0.1, v_epsilon=0.001, v_0=1, v_1=0.1,
        pressure=101325, fluid='IF97::Water'
    )
    assert round(bi_1, 7) == 0.9876953


def test_secant_method_velocity():
    se_1 = v_max_secant(
        0.4, 80, k=0.1, p_max=250, p_epsilon=1,
        v_0=1, v_1=2,
        pressure=101325, fluid='IF97::Water'
    )
    assert round(se_1, 7) == 3.7593294


def test_delta_p1():  # laminar
    dp = delta_p(1E-6, 1)
    assert round(dp, 13) == 1.00538E-8


def test_delta_p2():  # turb, Re < 10**5
    dp = delta_p(1, 5E-3, k=0.01)
    assert round(dp, 5) == 2743.41722


def test_delta_p3():  # turb, 10**5 < Re < 10**6
    dp = delta_p(10, 5E-3, k=0.001)
    assert round(dp, 5) == 156745.5396


def test_delta_p4():  # turb, Re > 10**6
    dp = delta_p(100, 5E-3, k=0.0001)
    assert round(dp, 5) == 10456325.31958


def test_delta_p5():  # turb, Re*k/di > 1300
    dp = delta_p(100, 5E-3, k=0.01)
    assert round(dp, 5) == 22592027.65789


def test_delta_p6():  # turb, transition
    dp = delta_p(100, 5E-3, k=0.0003)
    assert round(dp, 5) == 11865210.59373
