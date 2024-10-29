"""
Module for charting
"""
# Imports
# Standard Library Imports
import sys

# External Imports
from matplotlib import pyplot as plt

data1 = [
    [
        9,
        20,
        10,
        12,
        16,
        22,
        16,
        9,
        13,
        12,
        21,
        23,
        38,
        71,
        227,
        23,
        22,
        146,
        27,
        33,
        64,
        52,
        42,
        116,
        75,
        58,
        60,
        76,
        79,
        69,
        34,
        42,
        41,
        44,
        39,
        62,
        37,
        26,
        43,
        32,
        20,
        40,
        21,
        31,
        27,
        32,
        36,
        24,
        23,
        84,
        106,
        75,
        82,
        85,
        86,
        124,
        60,
        117,
        88,
    ],
    [
        12,
        11,
        8,
        7,
        10,
        8,
        9,
        7,
        19,
        7,
        20,
        306,
        18,
        58,
        216,
        243,
        31,
        17,
        28,
        23,
        34,
        52,
        37,
        34,
        44,
        42,
        39,
        27,
        49,
        28,
        31,
        25,
        31,
        57,
        37,
        35,
        35,
        36,
        50,
        30,
        25,
        37,
        26,
        29,
        26,
        23,
        29,
        18,
        22,
        22,
        104,
        100,
        67,
        93,
        81,
        123,
        63,
        64,
        75,
        51,
    ],
    [
        9,
        8,
        12,
        8,
        20,
        8,
        9,
        10,
        9,
        10,
        10,
        32,
        139,
        15,
        20,
        18,
        14,
        14,
        67,
        29,
        44,
        47,
        69,
        41,
        48,
        47,
        76,
        53,
        38,
        49,
        41,
        19,
        34,
        22,
        43,
        30,
        41,
        33,
        42,
        32,
        22,
        27,
        20,
        23,
        18,
        18,
        19,
        23,
        29,
        18,
        66,
        53,
        105,
        62,
        75,
        336,
        97,
        65,
        57,
        80,
    ],
    [
        12,
        9,
        6,
        11,
        18,
        34,
        10,
        8,
        5,
        51,
        76,
        182,
        14,
        8,
        10,
        18,
        12,
        124,
        19,
        17,
        28,
        17,
        26,
        24,
        22,
        27,
        63,
        30,
        56,
        71,
        23,
        39,
        24,
        18,
        28,
        27,
        18,
        19,
        22,
        30,
        21,
        19,
        13,
        10,
        15,
        16,
        12,
        14,
        11,
        10,
        101,
        39,
        27,
        78,
        40,
        71,
        39,
        43,
        59,
        61,
    ],
    [
        6,
        51,
        6,
        6,
        5,
        10,
        7,
        7,
        6,
        5,
        47,
        11,
        12,
        8,
        38,
        24,
        8,
        188,
        11,
        167,
        14,
        30,
        20,
        44,
        17,
        14,
        27,
        26,
        72,
        46,
        14,
        20,
        34,
        16,
        68,
        22,
        24,
        35,
        15,
        13,
        8,
        37,
        11,
        15,
        10,
        18,
        13,
        16,
        9,
        9,
        24,
        48,
        52,
        44,
        58,
        361,
        53,
        38,
        71,
        367,
    ],
    [
        6,
        23,
        9,
        7,
        6,
        10,
        9,
        29,
        8,
        46,
        12,
        20,
        16,
        9,
        172,
        8,
        44,
        6,
        112,
        9,
        17,
        63,
        25,
        36,
        79,
        14,
        71,
        17,
        39,
        19,
        23,
        19,
        26,
        18,
        9,
        15,
        10,
        28,
        12,
        18,
        16,
        17,
        12,
        11,
        10,
        15,
        8,
        15,
        10,
        21,
        45,
        27,
        39,
        1338,
        35,
        32,
        25,
        38,
        19,
        43,
    ],
]

data2 = [
    [
        0,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        0,
        7,
        8,
        14,
        23,
        53,
        8,
        8,
        56,
        10,
        13,
        26,
        17,
        16,
        52,
        30,
        22,
        24,
        30,
        33,
        24,
        12,
        15,
        13,
        16,
        12,
        24,
        12,
        8,
        15,
        11,
        5,
        12,
        6,
        9,
        8,
        11,
        12,
        8,
        7,
        31,
        46,
        28,
        34,
        30,
        37,
        54,
        23,
        53,
        40,
    ],
    [
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        4,
        0,
        7,
        6,
        13,
        82,
        82,
        9,
        5,
        8,
        8,
        10,
        16,
        11,
        12,
        14,
        15,
        12,
        10,
        19,
        10,
        11,
        8,
        9,
        22,
        13,
        12,
        12,
        12,
        19,
        7,
        8,
        13,
        8,
        9,
        8,
        8,
        9,
        4,
        5,
        5,
        45,
        42,
        25,
        39,
        32,
        46,
        24,
        23,
        28,
        19,
    ],
    [
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        8,
        58,
        4,
        6,
        5,
        4,
        4,
        20,
        8,
        15,
        15,
        24,
        13,
        15,
        15,
        31,
        19,
        11,
        17,
        13,
        5,
        11,
        5,
        12,
        8,
        14,
        10,
        15,
        9,
        6,
        7,
        5,
        6,
        4,
        5,
        5,
        7,
        10,
        5,
        19,
        19,
        34,
        20,
        22,
        38,
        25,
        20,
        31,
    ],
    [
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        22,
        73,
        3,
        1,
        2,
        4,
        3,
        42,
        5,
        3,
        7,
        2,
        4,
        6,
        6,
        6,
        17,
        9,
        19,
        30,
        7,
        13,
        6,
        3,
        7,
        8,
        2,
        4,
        5,
        8,
        6,
        4,
        3,
        2,
        4,
        4,
        2,
        2,
        2,
        1,
        42,
        11,
        4,
        27,
        12,
        26,
        11,
        14,
        18,
        23,
    ],
    [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        13,
        2,
        3,
        1,
        7,
        7,
        0,
        72,
        3,
        67,
        2,
        8,
        6,
        17,
        1,
        0,
        6,
        6,
        29,
        17,
        0,
        5,
        10,
        3,
        24,
        5,
        7,
        13,
        1,
        1,
        0,
        14,
        1,
        2,
        1,
        4,
        3,
        3,
        0,
        0,
        4,
        17,
        19,
        16,
        21,
        19,
        12,
        28,
    ],
    [
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        4,
        4,
        1,
        61,
        1,
        8,
        0,
        47,
        2,
        4,
        25,
        8,
        13,
        30,
        2,
        25,
        3,
        11,
        4,
        4,
        3,
        4,
        2,
        0,
        3,
        1,
        7,
        0,
        4,
        5,
        4,
        2,
        1,
        0,
        3,
        1,
        4,
        2,
        4,
        16,
        7,
        11,
        13,
        10,
        5,
        13,
        4,
        14,
    ],
]

data3 = [
    [
        56,
        96,
        97,
        107,
        112,
        130,
        108,
        102,
        87,
        73,
        84,
        140,
        84,
        79,
        102,
        134,
        104,
        69,
        64,
        121,
        88,
        96,
        123,
        132,
        99,
        93,
        113,
        104,
        121,
        91,
        90,
        66,
        118,
        117,
        59,
        136,
        69,
        103,
        89,
        118,
        132,
        87,
        83,
        83,
        122,
        74,
        89,
        81,
        97,
        143,
        62,
        140,
        105,
    ],
    [
        115,
        141,
        69,
        25,
        92,
        60,
        93,
        69,
        68,
        72,
        61,
        133,
        88,
        57,
        85,
        80,
        43,
        64,
        47,
        49,
        59,
        60,
        49,
        41,
        79,
        40,
        83,
        66,
        68,
        99,
        92,
        93,
        94,
        142,
        54,
        85,
        147,
        91,
        102,
        89,
        87,
        98,
        49,
        62,
        56,
        118,
        110,
        65,
        103,
        84,
        122,
        62,
        62,
        73,
        50,
    ],
    [
        99,
        41,
        112,
        75,
        13,
        68,
        7,
        34,
        74,
        45,
        22,
        85,
        43,
        63,
        53,
        46,
        44,
        86,
        62,
        63,
        98,
        53,
        60,
        62,
        124,
        78,
        46,
        69,
        100,
        41,
        86,
        38,
        90,
        63,
        106,
        80,
        115,
        71,
        72,
        80,
        60,
        73,
        51,
        63,
        58,
        76,
        111,
        53,
        51,
        50,
        89,
        54,
        59,
        101,
        66,
        52,
        81,
    ],
    [
        117,
        35,
        9,
        0,
        16,
        6,
        6,
        24,
        0,
        40,
        32,
        14,
        20,
        45,
        30,
        57,
        33,
        29,
        9,
        17,
        27,
        24,
        26,
        70,
        39,
        78,
        120,
        58,
        101,
        44,
        29,
        59,
        62,
        16,
        31,
        44,
        59,
        66,
        50,
        34,
        22,
        48,
        42,
        29,
        31,
        22,
        15,
        111,
        30,
        12,
        70,
        32,
        68,
        31,
        37,
        48,
        62,
    ],
    [
        1,
        87,
        19,
        3,
        0,
        0,
        15,
        3,
        16,
        0,
        128,
        28,
        29,
        12,
        71,
        75,
        9,
        30,
        8,
        31,
        23,
        69,
        7,
        0,
        25,
        25,
        119,
        71,
        6,
        38,
        79,
        27,
        39,
        52,
        99,
        13,
        8,
        2,
        13,
        24,
        17,
        44,
        40,
        41,
        9,
        7,
        13,
        45,
        51,
        44,
        57,
        52,
        33,
        74,
    ],
    [
        1,
        59,
        18,
        4,
        0,
        5,
        20,
        5,
        3,
        22,
        38,
        40,
        17,
        12,
        83,
        3,
        19,
        18,
        99,
        31,
        53,
        119,
        8,
        102,
        13,
        46,
        18,
        36,
        24,
        36,
        19,
        2,
        23,
        12,
        54,
        5,
        33,
        53,
        48,
        28,
        13,
        10,
        41,
        10,
        48,
        21,
        49,
        44,
        20,
        31,
        35,
        26,
        15,
        36,
        12,
        37,
    ],
]

data4 = [
    [
        47,
        102,
        101,
        72,
        119,
        141,
        108,
        110,
        95,
        87,
        33,
        138,
        102,
        75,
        119,
        142,
        70,
        73,
        77,
        123,
        88,
        94,
        114,
        138,
        119,
        101,
        113,
        99,
        116,
        76,
        97,
        66,
        127,
        125,
        70,
        117,
        85,
        116,
        92,
        134,
        77,
        88,
        92,
        43,
        128,
        147,
        143,
        48,
        108,
        79,
    ],
    [
        107,
        94,
        50,
        19,
        93,
        50,
        99,
        73,
        50,
        69,
        87,
        73,
        108,
        56,
        67,
        99,
        74,
        41,
        77,
        60,
        62,
        68,
        70,
        40,
        22,
        64,
        25,
        85,
        71,
        73,
        27,
        79,
        60,
        103,
        133,
        55,
        18,
        101,
        99,
        72,
        102,
        104,
        57,
        78,
        67,
        104,
        147,
        145,
        103,
        109,
        28,
        44,
    ],
    [
        102,
        36,
        108,
        81,
        13,
        74,
        7,
        36,
        64,
        48,
        25,
        101,
        30,
        60,
        59,
        42,
        48,
        94,
        78,
        61,
        101,
        65,
        68,
        70,
        116,
        91,
        56,
        86,
        102,
        36,
        90,
        38,
        62,
        22,
        100,
        70,
        114,
        77,
        90,
        83,
        75,
        81,
        49,
        42,
        66,
        96,
        55,
        64,
        90,
        73,
        95,
        91,
        101,
        129,
        102,
        91,
        132,
    ],
    [
        88,
        35,
        4,
        0,
        9,
        2,
        5,
        16,
        0,
        39,
        118,
        28,
        15,
        24,
        39,
        37,
        91,
        53,
        15,
        25,
        3,
        19,
        16,
        17,
        33,
        53,
        32,
        100,
        19,
        63,
        90,
        47,
        26,
        48,
        61,
        17,
        20,
        33,
        40,
        63,
        50,
        36,
        27,
        28,
        51,
        20,
        39,
        27,
        16,
        143,
        53,
        21,
        116,
        49,
        105,
        36,
        64,
        84,
        87,
    ],
    [
        1,
        38,
        21,
        1,
        0,
        0,
        15,
        0,
        10,
        0,
        117,
        21,
        31,
        6,
        83,
        27,
        10,
        112,
        34,
        138,
        11,
        42,
        2,
        73,
        6,
        0,
        26,
        25,
        56,
        74,
        6,
        30,
        81,
        26,
        139,
        40,
        10,
        90,
        11,
        9,
        2,
        10,
        10,
        21,
        55,
        50,
        51,
        9,
        9,
        18,
        37,
        81,
        77,
        93,
        91,
        57,
        101,
    ],
    [
        0,
        62,
        0,
        19,
        4,
        0,
        0,
        21,
        5,
        1,
        0,
        45,
        47,
        0,
        129,
        13,
        18,
        1,
        15,
        7,
        51,
        41,
        61,
        10,
        110,
        16,
        32,
        2,
        7,
        7,
        34,
        15,
        1,
        25,
        13,
        58,
        1,
        32,
        64,
        60,
        17,
        3,
        0,
        51,
        11,
        53,
        27,
        61,
        0,
        36,
        40,
        60,
        46,
        3,
        56,
        18,
        56,
    ],
]

data5 = [
    [
        44,
        96,
        95,
        68,
        112,
        133,
        101,
        103,
        89,
        78,
        29,
        124,
        92,
        67,
        107,
        128,
        70,
        73,
        77,
        123,
        88,
        94,
        114,
        138,
        119,
        101,
        113,
        99,
        116,
        76,
        97,
        66,
        127,
        125,
        70,
        117,
        85,
        116,
        92,
        134,
        77,
        88,
        92,
        32,
        97,
        112,
        108,
        37,
        82,
        60,
        138,
    ],
    [
        101,
        88,
        47,
        18,
        88,
        47,
        93,
        68,
        47,
        64,
        78,
        66,
        97,
        147,
        50,
        60,
        89,
        66,
        41,
        77,
        60,
        62,
        68,
        70,
        40,
        22,
        64,
        25,
        85,
        71,
        73,
        27,
        79,
        60,
        103,
        133,
        55,
        18,
        101,
        99,
        72,
        102,
        104,
        57,
        78,
        67,
        141,
        79,
        127,
        111,
        110,
        78,
        83,
        21,
        33,
    ],
    [
        96,
        34,
        101,
        76,
        13,
        70,
        7,
        33,
        60,
        45,
        23,
        91,
        146,
        27,
        54,
        53,
        38,
        43,
        142,
        85,
        78,
        61,
        101,
        65,
        68,
        70,
        116,
        91,
        56,
        86,
        102,
        36,
        90,
        38,
        62,
        22,
        100,
        70,
        114,
        77,
        90,
        83,
        75,
        81,
        49,
        42,
        66,
        96,
        55,
        64,
        68,
        55,
        120,
        72,
        69,
        77,
        98,
        77,
        69,
        100,
    ],
    [
        82,
        32,
        3,
        0,
        9,
        2,
        5,
        15,
        0,
        37,
        106,
        25,
        14,
        22,
        35,
        33,
        82,
        48,
        13,
        25,
        3,
        19,
        16,
        17,
        33,
        53,
        32,
        100,
        19,
        63,
        90,
        47,
        26,
        48,
        61,
        17,
        20,
        33,
        40,
        63,
        50,
        36,
        27,
        28,
        51,
        20,
        39,
        27,
        16,
        109,
        40,
        16,
        88,
        37,
        80,
        28,
        48,
        63,
        66,
    ],
    [
        1,
        36,
        19,
        1,
        0,
        0,
        14,
        0,
        10,
        0,
        106,
        18,
        27,
        6,
        75,
        25,
        9,
        101,
        30,
        124,
        11,
        42,
        2,
        73,
        6,
        0,
        26,
        25,
        56,
        74,
        6,
        30,
        81,
        26,
        139,
        40,
        10,
        90,
        11,
        9,
        2,
        10,
        10,
        21,
        55,
        50,
        51,
        9,
        9,
        14,
        28,
        61,
        59,
        70,
        69,
        43,
        76,
    ],
    [
        0,
        58,
        0,
        18,
        4,
        0,
        0,
        20,
        5,
        1,
        0,
        41,
        42,
        0,
        116,
        12,
        16,
        0,
        14,
        7,
        51,
        41,
        61,
        10,
        110,
        16,
        32,
        2,
        7,
        7,
        34,
        15,
        1,
        25,
        13,
        58,
        1,
        32,
        64,
        60,
        17,
        3,
        0,
        51,
        11,
        53,
        27,
        61,
        0,
        27,
        30,
        45,
        34,
        2,
        43,
        13,
        42,
    ],
]

data6 = [
    [
        60,
        100,
        99,
        75,
        117,
        139,
        113,
        0,
        93,
        78,
        93,
        119,
        0,
        93,
        69,
        107,
        137,
        99,
        66,
        63,
        100,
        112,
        92,
        103,
        119,
        132,
        108,
        93,
        113,
        99,
        112,
        90,
        119,
        90,
        63,
        117,
        117,
        63,
        147,
        73,
        99,
        79,
        115,
        134,
        86,
        83,
        0,
        125,
        77,
        95,
        86,
        102,
        65,
        137,
        110,
    ],
    [
        121,
        146,
        0,
        19,
        95,
        55,
        0,
        0,
        49,
        67,
        78,
        66,
        120,
        70,
        60,
        89,
        67,
        40,
        71,
        54,
        58,
        64,
        68,
        40,
        0,
        62,
        0,
        82,
        0,
        67,
        99,
        81,
        67,
        94,
        122,
        54,
        88,
        0,
        96,
        90,
        80,
        94,
        93,
        50,
        67,
        58,
        126,
        113,
        67,
        102,
        88,
        100,
        66,
        66,
        15,
        53,
    ],
    [
        102,
        0,
        0,
        80,
        0,
        0,
        7,
        35,
        63,
        0,
        23,
        91,
        27,
        62,
        57,
        51,
        43,
        84,
        72,
        66,
        105,
        63,
        63,
        67,
        112,
        87,
        51,
        78,
        100,
        38,
        83,
        38,
        80,
        62,
        85,
        80,
        104,
        71,
        77,
        73,
        65,
        71,
        48,
        67,
        63,
        82,
        120,
        55,
        54,
        53,
        95,
        57,
        59,
        61,
        78,
        61,
        55,
        87,
    ],
    [
        124,
        0,
        5,
        0,
        9,
        2,
        0,
        16,
        0,
        2,
        30,
        14,
        22,
        39,
        33,
        48,
        14,
        23,
        7,
        17,
        15,
        15,
        29,
        49,
        0,
        91,
        18,
        0,
        82,
        43,
        26,
        48,
        56,
        16,
        31,
        32,
        45,
        57,
        43,
        37,
        23,
        50,
        45,
        31,
        33,
        23,
        15,
        98,
        32,
        12,
        71,
        30,
        65,
        32,
        38,
        50,
        52,
    ],
    [
        0,
        37,
        0,
        1,
        0,
        0,
        15,
        0,
        12,
        0,
        115,
        26,
        28,
        10,
        75,
        62,
        10,
        31,
        10,
        37,
        28,
        6,
        6,
        0,
        23,
        28,
        51,
        66,
        5,
        27,
        78,
        24,
        37,
        9,
        82,
        10,
        8,
        2,
        76,
        9,
        26,
        18,
        47,
        43,
        44,
        8,
        7,
        12,
        11,
        50,
        46,
        56,
        55,
        34,
        61,
        0,
    ],
    [
        0,
        1,
        2,
        0,
        4,
        0,
        0,
        21,
        0,
        1,
        0,
        41,
        44,
        14,
        0,
        12,
        35,
        3,
        14,
        6,
        52,
        37,
        55,
        139,
        9,
        106,
        15,
        29,
        14,
        0,
        18,
        33,
        14,
        2,
        23,
        12,
        54,
        0,
        29,
        57,
        52,
        15,
        3,
        0,
        44,
        10,
        46,
        23,
        52,
        46,
        21,
        24,
        37,
        27,
        16,
        34,
        11,
        36,
    ],
]

data7 = [
    [
        60,
        100,
        98,
        74,
        116,
        137,
        112,
        107,
        92,
        75,
        89,
        113,
        88,
        66,
        102,
        130,
        102,
        66,
        63,
        100,
        112,
        92,
        103,
        118,
        132,
        107,
        93,
        113,
        99,
        112,
        90,
        118,
        90,
        63,
        117,
        117,
        63,
        147,
        73,
        99,
        79,
        115,
        134,
        86,
        83,
        79,
        121,
        74,
        92,
        83,
        99,
        145,
        63,
        132,
        106,
    ],
    [
        120,
        145,
        48,
        19,
        94,
        54,
        96,
        73,
        48,
        67,
        74,
        63,
        114,
        68,
        57,
        85,
        64,
        39,
        71,
        54,
        58,
        64,
        68,
        39,
        24,
        61,
        47,
        82,
        66,
        67,
        99,
        80,
        67,
        94,
        122,
        54,
        88,
        96,
        90,
        80,
        94,
        93,
        50,
        67,
        58,
        122,
        110,
        65,
        99,
        85,
        96,
        64,
        64,
        15,
        51,
    ],
    [
        101,
        43,
        106,
        79,
        13,
        72,
        7,
        35,
        63,
        47,
        22,
        86,
        26,
        59,
        54,
        49,
        41,
        80,
        72,
        66,
        104,
        63,
        63,
        66,
        112,
        87,
        51,
        78,
        100,
        38,
        83,
        38,
        80,
        62,
        85,
        80,
        104,
        71,
        77,
        73,
        65,
        71,
        48,
        67,
        63,
        82,
        120,
        55,
        52,
        52,
        92,
        55,
        57,
        59,
        76,
        59,
        53,
        84,
    ],
    [
        123,
        35,
        5,
        0,
        9,
        2,
        5,
        16,
        0,
        2,
        28,
        13,
        20,
        37,
        31,
        46,
        13,
        23,
        7,
        17,
        15,
        15,
        29,
        49,
        34,
        91,
        18,
        58,
        82,
        43,
        26,
        48,
        56,
        16,
        31,
        32,
        45,
        57,
        43,
        37,
        23,
        50,
        45,
        31,
        33,
        23,
        15,
        95,
        31,
        12,
        69,
        29,
        63,
        31,
        37,
        49,
        50,
    ],
    [
        1,
        37,
        20,
        1,
        0,
        0,
        14,
        0,
        12,
        0,
        109,
        25,
        27,
        9,
        71,
        59,
        9,
        30,
        10,
        37,
        28,
        6,
        6,
        0,
        23,
        28,
        51,
        66,
        5,
        27,
        78,
        24,
        37,
        9,
        82,
        10,
        8,
        2,
        76,
        9,
        26,
        18,
        47,
        43,
        44,
        8,
        7,
        11,
        13,
        49,
        45,
        55,
        53,
        33,
        59,
    ],
    [
        0,
        1,
        2,
        19,
        4,
        0,
        0,
        20,
        5,
        1,
        0,
        39,
        41,
        14,
        0,
        12,
        32,
        3,
        13,
        6,
        52,
        37,
        55,
        139,
        9,
        106,
        15,
        29,
        14,
        0,
        18,
        33,
        14,
        2,
        23,
        12,
        54,
        0,
        29,
        57,
        52,
        15,
        3,
        0,
        44,
        10,
        46,
        23,
        52,
        45,
        21,
        23,
        36,
        26,
        16,
        33,
        10,
        34,
    ],
]

data8 = [
    [
        60,
        100,
        98,
        74,
        116,
        137,
        112,
        107,
        92,
        75,
        89,
        113,
        88,
        66,
        102,
        130,
        102,
        66,
        63,
        100,
        112,
        92,
        103,
        118,
        132,
        107,
        93,
        113,
        99,
        112,
        90,
        118,
        90,
        63,
        117,
        117,
        63,
        147,
        73,
        99,
        79,
        115,
        134,
        86,
        83,
        79,
        121,
        74,
        92,
        83,
        99,
        145,
        63,
        132,
        106,
    ],
    [
        120,
        145,
        48,
        19,
        94,
        54,
        96,
        73,
        48,
        67,
        74,
        63,
        114,
        68,
        57,
        85,
        64,
        39,
        71,
        54,
        58,
        64,
        68,
        39,
        24,
        61,
        47,
        82,
        66,
        67,
        99,
        80,
        67,
        94,
        122,
        54,
        88,
        96,
        90,
        80,
        94,
        93,
        50,
        67,
        58,
        122,
        110,
        65,
        99,
        85,
        96,
        64,
        64,
        15,
        51,
    ],
    [
        101,
        43,
        106,
        79,
        13,
        72,
        7,
        35,
        63,
        47,
        22,
        86,
        26,
        59,
        54,
        49,
        41,
        80,
        72,
        66,
        104,
        63,
        63,
        66,
        112,
        87,
        51,
        78,
        100,
        38,
        83,
        38,
        80,
        62,
        85,
        80,
        104,
        71,
        77,
        73,
        65,
        71,
        48,
        67,
        63,
        82,
        120,
        55,
        52,
        52,
        92,
        55,
        57,
        59,
        76,
        59,
        53,
        84,
    ],
    [
        123,
        35,
        5,
        9,
        2,
        5,
        16,
        2,
        28,
        13,
        20,
        37,
        31,
        46,
        13,
        23,
        7,
        17,
        15,
        15,
        29,
        49,
        34,
        91,
        18,
        58,
        82,
        43,
        26,
        48,
        56,
        16,
        31,
        32,
        45,
        57,
        43,
        37,
        23,
        50,
        45,
        31,
        33,
        23,
        15,
        95,
        31,
        12,
        69,
        29,
        63,
        31,
        37,
        49,
        50,
    ],
    [
        1,
        37,
        20,
        1,
        14,
        0,
        12,
        109,
        25,
        27,
        9,
        71,
        59,
        9,
        30,
        10,
        37,
        28,
        6,
        6,
        0,
        23,
        28,
        51,
        66,
        5,
        27,
        78,
        24,
        37,
        9,
        82,
        10,
        8,
        2,
        76,
        9,
        26,
        18,
        47,
        43,
        44,
        8,
        7,
        11,
        13,
        49,
        45,
        55,
        53,
        33,
        59,
    ],
    [
        0,
        1,
        2,
        19,
        4,
        0,
        0,
        20,
        5,
        1,
        39,
        41,
        14,
        0,
        12,
        32,
        3,
        13,
        6,
        52,
        37,
        55,
        139,
        9,
        106,
        15,
        29,
        14,
        0,
        18,
        33,
        14,
        2,
        23,
        12,
        54,
        29,
        57,
        52,
        15,
        3,
        0,
        44,
        10,
        46,
        23,
        52,
        45,
        21,
        23,
        36,
        26,
        16,
        33,
        10,
        34,
    ],
]

data9 = [
    [
        53,
        88,
        87,
        103,
        121,
        99,
        75,
        89,
        113,
        88,
        66,
        102,
        130,
        106,
        68,
        66,
        104,
        116,
        96,
        106,
        123,
        111,
        93,
        113,
        99,
        112,
        90,
        118,
        90,
        63,
        117,
        132,
        71,
        82,
        89,
        129,
        94,
        80,
        122,
        75,
        93,
        84,
        99,
        146,
        63,
        133,
    ],
    [
        106,
        128,
        83,
        48,
        59,
        74,
        63,
        68,
        57,
        85,
        64,
        41,
        74,
        56,
        60,
        67,
        70,
        41,
        64,
        82,
        67,
        99,
        80,
        67,
        94,
        122,
        54,
        99,
        109,
        101,
        90,
        106,
        57,
        75,
        123,
        110,
        65,
        100,
        86,
        65,
        64,
        15,
        52,
    ],
    [
        89,
        70,
        11,
        6,
        55,
        22,
        86,
        26,
        59,
        54,
        49,
        41,
        80,
        75,
        68,
        108,
        65,
        69,
        90,
        52,
        81,
        100,
        38,
        83,
        38,
        80,
        62,
        80,
        104,
        71,
        87,
        73,
        54,
        76,
        71,
        93,
        136,
        62,
        53,
        52,
        92,
        56,
        57,
        59,
        76,
        60,
        53,
        84,
    ],
    [
        4,
        2,
        4,
        14,
        28,
        13,
        20,
        37,
        31,
        46,
        13,
        24,
        18,
        16,
        16,
        30,
        50,
        94,
        18,
        82,
        43,
        48,
        56,
        31,
        32,
        45,
        65,
        41,
        26,
        56,
        51,
        35,
        37,
        26,
        17,
        95,
        31,
        12,
        69,
        29,
        64,
        32,
        37,
        49,
        51,
    ],
    [
        1,
        18,
        1,
        13,
        10,
        109,
        25,
        27,
        9,
        71,
        59,
        9,
        30,
        10,
        7,
        6,
        24,
        29,
        53,
        69,
        5,
        27,
        78,
        24,
        37,
        9,
        82,
        10,
        8,
        2,
        85,
        10,
        29,
        20,
        54,
        48,
        9,
        8,
        11,
        13,
        49,
        45,
        54,
        33,
        59,
        47,
    ],
    [
        2,
        17,
        4,
        0,
        18,
        5,
        1,
        39,
        14,
        0,
        12,
        3,
        13,
        7,
        54,
        39,
        57,
        144,
        10,
        109,
        15,
        30,
        15,
        0,
        18,
        33,
        14,
        2,
        23,
        12,
        54,
        29,
        64,
        3,
        0,
        50,
        11,
        51,
        26,
        59,
        45,
        21,
        23,
        36,
        16,
        33,
        10,
        35,
    ],
]

labels = ["0", "3.13", "6.25", "12.5", "25.0", "50.0"]


def boxplot():
    fig, axs = plt.subplots(nrows=3, ncols=3, figsize=[16, 12], sharey=True)

    axs[0, 0].set_title("Iteration 1")
    axs[0, 0].boxplot(
        data1,
        labels=labels,
        meanline=True,
        showfliers=False,
        showmeans=True,
        whis=(0, 95),
    )
    axs[0, 1].set_title("Iteration 2\nexclusion = 1.4%")
    axs[0, 1].boxplot(
        data2, labels=labels, meanline=True, showmeans=True, whis=(0, 100)
    )
    axs[0, 2].set_title("Iteration 3\nexclusion = 7.5%")
    axs[0, 2].boxplot(
        data3, labels=labels, meanline=True, showmeans=True, whis=(0, 100)
    )
    axs[1, 0].set_title("Iteration 4\nexclusion = 7.5%")
    axs[1, 0].boxplot(
        data4, labels=labels, meanline=True, showmeans=True, whis=(0, 100)
    )
    axs[1, 1].set_title("Iteration 5\nexclusion = 5.6%")
    axs[1, 1].boxplot(
        data5, labels=labels, meanline=True, showmeans=True, whis=(0, 100)
    )
    axs[1, 2].set_title("Iteration 6\nexclusion = 5.3%")
    axs[1, 2].boxplot(
        data6, labels=labels, meanline=True, showmeans=True, whis=(0, 100)
    )
    axs[2, 0].set_title("Iteration 7\nexclusion = 5.8%")
    axs[2, 0].boxplot(
        data7, labels=labels, meanline=True, showmeans=True, whis=(0, 100)
    )
    axs[2, 1].set_title("Iteration 8\nexclusion = 7.8%")
    axs[2, 1].boxplot(
        data8, labels=labels, meanline=True, showmeans=True, whis=(0, 100)
    )
    axs[2, 2].set_title("Iteration 9\nexclusion = 23.1%")
    axs[2, 2].boxplot(
        data9, labels=labels, meanline=True, showmeans=True, whis=(0, 100)
    )

    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    plt.savefig("chart.png")