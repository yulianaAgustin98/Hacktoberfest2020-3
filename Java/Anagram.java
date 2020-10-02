 public boolean isAnAnagram(String[] words) {
        return Stream.of(words)
                .map(String::chars).map(IntStream::sorted)
                .map(IntStream::toArray).map(Arrays::toString)
                .distinct().count() == 1;
    }
