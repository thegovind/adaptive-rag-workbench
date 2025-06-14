import React from 'react';

export function CitigroupLogo() {
  return (
    <div className="flex items-center space-x-2">
      <div className="w-8 h-8 bg-citigroup-blue rounded flex items-center justify-center">
        <span className="text-white font-bold text-sm">C</span>
      </div>
      <span className="text-citigroup-blue font-semibold text-sm">Citigroup</span>
    </div>
  );
}
