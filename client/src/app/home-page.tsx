"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { Rocket, BrainCircuit, BookOpenText } from "lucide-react";
import { Skeleton } from "@/components/ui/skeleton";

export default function HomePage() {
  const [hasSentMessage, setHasSentMessage] = useState(false);
  const [inputValue, setInputValue] = useState("");

  const exampleQueries = [
    "Explain quadratic equations",
    "How does calculus work?",
    "Show matrix operations",
  ];

  return (
    <div className="flex flex-col min-h-screen bg-zinc-50 dark:bg-zinc-900">
      <main className="flex-1 flex items-center justify-center py-12 px-4 sm:px-8"> {/* Added centering */}
        <div className="max-w-4xl w-full flex flex-col gap-8 mt-[-50px]"> {/* Added negative margin */}
          {/* Animated Landing Header */}
          <div className={`transition-all duration-500 overflow-hidden ${
            hasSentMessage ? "opacity-0 h-0" : "opacity-100 h-auto"
          }`}>
            <div className="flex flex-col items-center text-center gap-6">
              <div className="bg-zinc-100 dark:bg-zinc-800 p-6 rounded-2xl">
                <BrainCircuit className="h-16 w-16 text-zinc-900 dark:text-zinc-50 mx-auto" />
              </div>
              
              <h1 className="text-5xl font-bold text-zinc-900 dark:text-zinc-50">
              {" "}
                <code className="bg-black/[.05] dark:bg-white/[.06] px-1 py-0.5 rounded font-semibold">
                  CMath
                </code>
              </h1>
              
              <p className="text-xl text-zinc-600 dark:text-zinc-400 max-w-2xl">
                Your personal mathematics assistant powered by AI
              </p>

              <div className="grid grid-cols-2 gap-4 mt-4 w-full">
                <div className="bg-zinc-100 dark:bg-zinc-800 p-6 rounded-2xl">
                  <BookOpenText className="h-8 w-8 text-zinc-900 dark:text-zinc-50 mb-4" />
                  <h3 className="text-lg font-semibold mb-2 text-zinc-900 dark:text-zinc-50">
                    Concept Library
                  </h3>
                  <p className="text-sm text-zinc-600 dark:text-zinc-400">
                    Explore mathematical concepts from algebra to calculus
                  </p>
                </div>

                <div className="bg-zinc-100 dark:bg-zinc-800 p-6 rounded-2xl">
                  <Rocket className="h-8 w-8 text-zinc-900 dark:text-zinc-50 mb-4" />
                  <h3 className="text-lg font-semibold mb-2 text-zinc-900 dark:text-zinc-50">
                    Instant Help
                  </h3>
                  <p className="text-sm text-zinc-600 dark:text-zinc-400">
                    Get step-by-step solutions within seconds
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Video Skeleton with Text */}
          {hasSentMessage && (
            <div className="animate-in fade-in slide-in-from-bottom-4 space-y-4">
              <Skeleton className="h-[400px] w-full rounded-2xl bg-zinc-200 dark:bg-zinc-700" />
              <div className="space-y-2">
                <Skeleton className="h-4 w-[250px] bg-zinc-200 dark:bg-zinc-700" />
                <Skeleton className="h-4 w-[200px] bg-zinc-200 dark:bg-zinc-700" />
              </div>
            </div>
          )}

          {/* Input Area */}
          <div className="sticky bottom-8 bg-zinc-100 dark:bg-zinc-800 p-6 rounded-2xl">
            <div className="relative">
              <Textarea
                placeholder="Ask me anything about mathematics..."
                className="pl-6 pr-20 py-5 min-h-[120px] text-xl rounded-xl focus-visible:ring-2 focus-visible:ring-zinc-900 dark:focus-visible:ring-zinc-50 resize-none bg-white dark:bg-zinc-900 border-none"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
              />
              <Button
                onClick={() => setHasSentMessage(true)}
                variant="default"
                size="icon"
                className="absolute bottom-4 right-4 h-12 w-12 rounded-xl bg-zinc-900 hover:bg-zinc-800 dark:bg-zinc-50 dark:hover:bg-zinc-100"
              >
                <Rocket className="h-6 w-6 text-zinc-50 dark:text-zinc-900" />
              </Button>
            </div>
            
            {/* Example Queries */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-3 mt-4"> {/* Changed to 3 columns */}
              {exampleQueries.map((query, index) => (
                <Button
                  key={index}
                  variant="outline"
                  className="h-10 text-left justify-start hover:bg-zinc-200 dark:hover:bg-zinc-700 rounded-lg font-semibold" // Added font-semibold
                  onClick={() => setInputValue(query)}
                >
                  <span className="text-zinc-900 dark:text-zinc-50 truncate">{query}</span>
                </Button>
              ))}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}