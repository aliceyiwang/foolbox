import pytest
import numpy as np

from foolbox.attacks import AdditiveUniformNoiseAttack
from foolbox.attacks import AdditiveGaussianNoiseAttack

Attacks = [
    AdditiveUniformNoiseAttack,
    AdditiveGaussianNoiseAttack,
]


@pytest.mark.parametrize('Attack', Attacks)
def test_attack(Attack, bn_adversarial):
    adv = bn_adversarial
    attack = Attack()
    attack(adv)
    assert adv.get() is not None
    assert adv.best_distance().value() < np.inf


@pytest.mark.parametrize('Attack', Attacks)
def test_attack_gl(Attack, gl_bn_adversarial):
    adv = gl_bn_adversarial
    attack = Attack()
    attack(adv)
    assert adv.get() is not None
    assert adv.best_distance().value() < np.inf


@pytest.mark.parametrize('Attack', Attacks)
def test_attack_impossible(Attack, bn_impossible):
    adv = bn_impossible
    attack = Attack()
    attack(adv)
    assert adv.get() is None
    assert adv.best_distance().value() == np.inf
